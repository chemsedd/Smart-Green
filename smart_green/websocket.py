from json import loads, dumps
from sg_dashboard.scripts.consumer import consumer_kafka
from asgiref.sync import sync_to_async


async def websocket_application(scope, receive, send):
    event = await receive()
    # Client is asking for connectiong
    if event['type'] == 'websocket.connect':
        await send({
            'type': 'websocket.accept'
        })
        # Create kafka consumer
        consumer = consumer_kafka()
        message = None

    await send({
        'type': 'websocket.send',
        'text': 'start!'
    })
    from sg_dashboard.models import Daily_real_time
    while True:
        # listen to websocket
        print('blocking here...\n')
        event = await receive()
        print('after blocking ...\n')
        # Client disconnecting
        if event['type'] == 'websocket.disconnect':
            break
        # Client sending a message
        elif event['type'] == 'websocket.receive':
            if event['text'] == 'next':
                # listening to producer
                message = next(consumer)
                data: dict = loads(message.value)
                daily_real_time = Daily_real_time()
                daily_real_time.humidity = float(data['humidity']['value'])
                daily_real_time.temperature = float(
                    data['temperature']['value'])
                daily_real_time.moisture = float(data['moisture']['value'])
                async_save = sync_to_async(daily_real_time.save)
                await async_save()
                # send data to update charts
                await send({
                    'type': 'websocket.send',
                    'text': dumps(data)
                })
