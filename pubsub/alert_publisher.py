from google.cloud import pubsub_v1
import json
import uuid

publisher = pubsub_v1.PublisherClient()
topic_path = publisher.topic_path("transactions-466418", "suspicious-alerts")

def publish_alert(transaction):
    alert = {
        "alert_id": str(uuid.uuid4()),
        "transaction_id": transaction["transaction_id"],
        "risk_score": transaction["risk_score"],
        "reason": "High risk transaction",
        "alert_time": transaction["timestamp"]
    }
    publisher.publish(topic_path, json.dumps(alert).encode("utf-8"))