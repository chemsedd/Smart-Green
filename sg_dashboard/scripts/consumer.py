"""
    SmartGreen Consumer
    -------------------
    - This code resides on the Server app, the server acts as a consumer to the data sent by the producer.
    - The server is resposible for Displaying and Storing the comming data.
"""

from kafka import KafkaConsumer
from json import loads


# Creates a consumer and returns it
def consumer_kafka():
    #   start kafka Consumer to receive data from the raspberry pi
    #   Raspberry pi (producer) ====> Kafka (consumer) ====> Websocket
    topic = 'WeatherData'
    consumer = KafkaConsumer(topic, bootstrap_servers=['localhost:9092'])

    print('Kafka Consumer started... ✔')
    print('---------------------------')

    return consumer
