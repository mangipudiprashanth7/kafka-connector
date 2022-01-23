from kafka import KafkaProducer
from kafka import KafkaConsumer

from constants import *
import json

VALUE_SERIALIZER = lambda v: json.dumps(v).encode("utf-8")
VALUE_DESERIALIZER = lambda m: json.loads(m.decode("utf-8"))


def consumeMessages():
    consumer = KafkaConsumer(
        "first",
        bootstrap_servers=[KAFKA_SERVER_1],
        api_version=(0, 10, 1),
        group_id="topic-group",
        value_deserializer=VALUE_DESERIALIZER,
    )
    print("starting consumer")
    for msg in consumer:
        print(msg)


consumeMessages()
