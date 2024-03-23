import json
import time

from kafka import KafkaProducer

KAFKA_TOPIC = "order_details"
ORDER_LIMIT = 15

producer = KafkaProducer(bootstrap_servers = "localhost:29092")

print("Will start generating Orders after 10 seconds")

for i in range(ORDER_LIMIT):
    data ={ 
        "user_id" : f"pk_{i}",
        "order_id" : 1,
        "item" : "Burger"
    }
    
    producer.send(
        KAFKA_TOPIC,
        json.dumps(data).encode("utf-8")
    )
    
    print(f"Done sending ----{i}")
    time.sleep(2)