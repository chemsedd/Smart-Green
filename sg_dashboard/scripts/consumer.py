"""
    SmartGreen Consumer
    -------------------
    - This code resides on the Server app, the server acts as a consumer to the data sent by the producer.
    - The server is resposible for Displaying and Storing the comming data.
"""

from kafka import KafkaConsumer
from json import loads
#from .websocket.websocket import new_data, start_websocket


#
def consumer_kafka():
    #   start kafka Consumer to receive data from the raspberry pi
    #   Raspberry pi (producer) ====> Kafka (consumer) ====> Websocket
    topic = 'WeatherData'
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

    print('Kafka Consumer started... ✔')
    print('---------------------------')
    # receiving messages from producer
    for message in consumer:
        data: dict = loads(message.value)
        for k, v in data.items():
            print(f'{k} --> {v}')
        print('-' * 30)
        new_data = data
