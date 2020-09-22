from time import sleep
from kafka import KafkaProducer
from json import dumps
import random
from datetime import date, time

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', value_serializer=lambda msg: dumps(msg).encode('utf-8'))

while True:
    date_ = str(date.today())
    #time_ = str()
    data = {
        'temperature': {
            'value': random.randint(0, 80),
            'date': date_
        },
        'humidity': {
            'value': random.randint(0, 100),
            'date': date_
        },
        'moisture': {
            'value': random.randint(0, 100),
            'date': date_
        },
    }
    producer.send('WeatherData', data)
    producer.flush()
    print('sent...\n')
    sleep(1)
