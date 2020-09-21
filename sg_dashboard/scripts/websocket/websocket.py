import asyncio
import websockets
import json


# Store the new collected values
new_data = None


#
#   Send data to the client side to update charts
#   Data is sent through websockets.
#
async def updateCharts(websocket, path):
    global new_data
    while True:
        data = {
            'temperature': 24,
            'humidity': 80,
            'ph': 5,
            'moisture': 70,
        }
        if new_data != None:
            await websocket.send(json.dumps(new_data))
            print(f'Message sent: {new_data}')
            await asyncio.sleep(5)


#
#   Start websocket with the given task.
#
async def start_websocket():
    start_server = websockets.serve(updateCharts, "localhost", 5000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
