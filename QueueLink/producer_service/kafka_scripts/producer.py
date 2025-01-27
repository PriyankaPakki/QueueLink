# To send messages to Q1


from kafka import KafkaProducer, KafkaConsumer


def produce_messages():
    producer = KafkaProducer(bootstrap_servers="kafka:9092")
    message = "Hello from ProducerService"

    producer.send("Q1", message.encode())
    producer.flush()

    print(f"Message sent to Q1: {message}")


def consume_acknowledgments():
    consumer = KafkaConsumer(
        "Q2",
        bootstrap_servers="kafka:9092",
        auto_offset_reset="earliest",
        group_id="producer-group",
    )
    print(" Waiting acknowledgements")

    ack_count = 0
    for message in consumer:
        print(f"Acknowledgement received: {message.value.decode()}")
        ack_count += 1
        if ack_count == 2:
            break


if __name__ == "__main__":
    produce_messages()
    consume_acknowledgments()
