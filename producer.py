from time import sleep
from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', value_serializer=lambda msg: dumps(msg).encode('utf-8'))

while True:
    data = {
        'temperature': 23,
        'humidity': 40,
        'moisture': 20,
        'pH': 6,
    }
    producer.send('WeatherData', data)
    producer.flush()
    print('sent...\n')
    sleep(5)
