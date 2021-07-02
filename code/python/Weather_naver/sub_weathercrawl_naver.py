from kafka import KafkaConsumer
from json import loads

def subscribe():
    # topic, broker list
    consumer = KafkaConsumer(
        'weather',
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id='my-group',
        value_deserializer=lambda x: loads(x.decode('utf-8')),
        consumer_timeout_ms=1000,
        api_version=(2, 0, 2)
    )

    # consumer list를 가져온다
    print('[begin] get consumer list')
    for message in consumer:
        print("Topic: %s, Partition: %d, Offset: %d, Key: %s, Value: %s" %
              (message.topic, message.partition, message.offset, message.key, message.value)
              )
        print('[end] get consumer list')


if __name__ == "__main__":
    subscribe()