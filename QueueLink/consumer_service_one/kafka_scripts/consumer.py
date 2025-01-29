from kafka import KafkaConsumer


def consume_messages():
    consumer = KafkaConsumer(
        "Q1",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        group_id="shared-consumer-group",
    )

    counter = 0
    for message in consumer:
        print(f" Consumer service one processed {message.value.decode()}")
        counter += 1

    print(f"consumer one processed {counter} messages")


if __name__ == "__main__":
    consume_messages()
