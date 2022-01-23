from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "firsttopic1",
        bootstrap_servers="44.202.122.4:9092",
        auto_offset_reset="earliest",
        api_version=(0, 10, 1),
    )
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))
