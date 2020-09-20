"""
    SmartGreen Consumer
    -------------------
    - This code resides on the Server app, the server acts as a consumer to the data sent by the producer.
    - The server is resposible for Displaying and Storing the comming data.
"""

from kafka import KafkaConsumer
from json import loads
from .websocket.websocket import start_websocket, updateCharts


#
def send_charts_data(data):
    pass


#
def consumer_kafka():
    #   start kafka Consumer to receive data from the raspberry pi
    #   Raspberry pi (producer) ====> Kafka (consumer) ====> Websocket
    topic = 'WeatherData'
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

    #   Start websocket
    #   Websocket ====> front end
    # start_websocket(updateCharts)

    print('Kafka Consumer started... ✔')
    print('---------------------------')
    # receiving messages from producer
    for message in consumer:
        data: dict = loads(message.value)
        for k, v in data.items():
            print(f'{k} --> {v}')
        print('-' * 30)
        # send data to front end to update charts
        # send_charts_data(data)
