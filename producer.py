from threading import Thread
from kafka import KafkaProducer
import json
from data import get_registered_user
import time
from constants import *


def json_serializer(data):
    return json.dumps(data).encode("utf-8")


class Producer(Thread):
    def run(self):
        producer = KafkaProducer(
            bootstrap_servers=[KAFKA_SERVER_1],
            value_serializer=json_serializer,
            api_version=(0, 10, 1),
        )
        print("starting the producer")
        x = 10
        idx = 0
        while idx != x:
            registered_user = get_registered_user()
            print(registered_user)
            producer.send(TOPIC_NAME_1, registered_user)
            time.sleep(4)
            idx += 1


if __name__ == "__main__":
    print("producer-main::Starting")
