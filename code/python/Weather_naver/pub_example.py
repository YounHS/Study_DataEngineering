import sys
import json
from kafka import KafkaProducer
from kafka.errors import KafkaError


producer = KafkaProducer(bootstrap_servers=["localhost:9092"])
topicName = "test"
msg = {"id":"test", "tel":"010-1234-5678", "regDate":"20201109"}

def on_send_success(record_metadata):
    print(record_metadata.topic)
    print(record_metadata.partition)
    print(record_metadata.offset)

# def on_send_error(excp):
#     log.error("error!!!", exc_info=excp)

producer = KafkaProducer(value_serializer=lambda m: json.dumps(msg).encode("ascii"))
producer.send(topicName, {'key':'value'}).add_callback(on_send_success)

producer.flush()

producer = KafkaProducer(retries=5)