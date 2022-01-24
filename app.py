import concurrent.futures

from consumer import *
from producer import *

if __name__ == "__main__":
    print("main::Starting")

    consumer = Consumer()
    producer = Producer()
    consumer.start()
    producer.start()

    consumer.join()
    producer.join()
