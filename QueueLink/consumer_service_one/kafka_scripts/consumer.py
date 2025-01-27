from kafka import KafkaConsumer, KafkaProducer


def consume_and_acknowledge():
    consumer = KafkaConsumer(
        "Q1",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        group_id="consumer-one-group",
    )

    producer = KafkaProducer(bootstrap_servers="kafka:9092")

    for message in consumer:
        print(f" Consumer service one recieved {message.value.decode()}")
        producer.send("Q2", b"Consumer service one: I recieved")
        producer.flush()
        print("Acknowledgement sent to Q2")


if __name__ == "__main__":
    consume_and_acknowledge()
