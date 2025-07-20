import json
import time
import random
from kafka import KafkaProducer

producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    api_version=(2, 8, 0),
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def generate_transaction():
    return {
        "transaction_id": f"txn_{random.randint(1000,9999)}",
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "account_id": f"acct_{random.randint(100,999)}",
        "amount": round(random.uniform(100, 20000), 2),
        "currency": "USD",
        "to_account": f"acct_{random.randint(100,999)}",
        "location": random.choice(["USA", "Iran", "UK", "India", "North Korea"]),
        "channel": random.choice(["Online", "ATM", "POS"]),
        "device_id": f"dev_{random.randint(1000,9999)}"
    }

while True:
    txn = generate_transaction()
    producer.send('transactions', txn)
    print(f"Sent: {txn}")
    time.sleep(1)