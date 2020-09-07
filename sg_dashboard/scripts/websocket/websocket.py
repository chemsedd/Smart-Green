import asyncio
import websockets
import json


#
#   Send data to the client side to update charts
#   Data is sent through websockets.
#
async def updateCharts(websocket, path):
    while True:
        data = {
            'temperature': 24,
            'humidity': 80,
            'ph': 5,
            'moisture': 70,
        }
        await websocket.send(json.dumps(data))
        print(f'Message sent: {data}')
        await asyncio.sleep(5)


#
#   Start websocket with the given task.
#
def start_websocket(fun):
    start_server = websockets.serve(fun, "localhost", 5000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
