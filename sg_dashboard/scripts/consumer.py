"""
    SmartGreen Consumer
    -------------------
    - This code resides on the Server app, the server acts as a consumer to the data sent by the producer.
    - The server is resposible for Displaying and Storing the comming data.
"""

from kafka import KafkaConsumer
from json import loads


def consumer_kafka():
    print('Kafka Consumer started... ✔')
    print('---------------------------')
    consumer = KafkaConsumer(
        'WeatherData', bootstrap_servers=['localhost:9092'])
    # receiving messages from producer
    for message in consumer:
        data: dict = loads(message.value)
        for k, v in data.items():
            print(f'{k} --> {v}')
        print('-' * 30)
