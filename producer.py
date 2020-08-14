from kafka import KafkaProducer
from json import dumps

producer = KafkaProducer(
    bootstrap_servers='localhost:9092', value_serializer=lambda msg: dumps(msg).encode('utf-8'))

data = {
    'Temperature': 23,
    'Humidity': 40,
    'Pressure': 20,
    'pH': 6,
}
producer.send('WeatherData', data)
producer.flush()
