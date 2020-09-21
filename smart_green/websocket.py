from sg_dashboard.scripts.consumer import consumer_kafka
from json import loads, dumps
import asyncio


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        # Client is asking for connectiong
        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })
            # Create kafka consumer
            consumer = consumer_kafka()
            # listening to producer
            for message in consumer:
                data: dict = loads(message.value)
                for k, v in data.items():
                    print(f'{k} --> {v}')
                print('-' * 30)
                # send data to update charts
                await send({
                    'type': 'websocket.send',
                    'text': dumps(data)
                })
        # Client disconnecting
        elif event['type'] == 'websocket.disconnect':
            break
        # Client sending a message
        elif event['type'] == 'websocket.receive':
            if event['text'] == 'send_data':
                await send({
                    'type': 'websocket.send',
                    'text': 'pong!!!!'
                })
