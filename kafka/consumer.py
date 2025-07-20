from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    'transactions',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))
)

print("Starting consumer...")
for message in consumer:
    print(f"Received: {message.value}")