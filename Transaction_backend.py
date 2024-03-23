import json

from kafka import KafkaConsumer,KafkaProducer

Kafka_Topic = "order_details"

consumer = KafkaConsumer(
    Kafka_Topic,
    bootstrap_servers = "localhost:29092"
)

producer = KafkaProducer(
    bootstrap_servers = "localhost:29092"
)

print("Gonna Start Listening...")

while True:
    for message in consumer:
        print("Ongoing Transaction..")
        consumed_message = json.loads( message.value.decode() )
        print(consumed_message)
