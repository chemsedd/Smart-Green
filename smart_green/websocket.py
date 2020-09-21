from json import dumps


async def websocket_application(scope, receive, send):
    while True:
        event = await receive()
        # Client is asking for connectiong
        if event['type'] == 'websocket.connect':
            await send({
                'type': 'websocket.accept'
            })
        # Client disconnecting
        elif event['type'] == 'websocket.disconnect':
            break
        # Client sending a message
        elif event['type'] == 'websocket.receive':
            if event['text'] == 'send_data':
                data = {
                    'temperature': 23,
                    'humidity': 80,
                    'moisture': 50
                }
                await send({
                    'type': 'websocket.send',
                    'text': dumps(data)
                })
