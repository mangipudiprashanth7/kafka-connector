from concurrent.futures import thread
from threading import Thread
from kafka import KafkaConsumer
import json
from constants import *


class Consumer(Thread):
    def run(self):
        consumer = KafkaConsumer(
            TOPIC_NAME_1,
            bootstrap_servers=KAFKA_SERVER_1,
            auto_offset_reset="earliest",
            api_version=(0, 10, 1),
        )
        print("starting the consumer")
        for msg in consumer:
            print("Registered User = {}".format(json.loads(msg.value)))


if __name__ == "__main__":
    print("consumer-main::Starting")
