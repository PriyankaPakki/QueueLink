# To send messages to Q1


# from kafka import KafkaProducer


class KafkaMessageProducer:
    pass
    # def __init__(self, bootstrap_servers="kafka:9092"):
    #     self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    # def produce_messages(self, topic, num_messages):
    #     for i in range(num_messages):
    #         message = f"Message {i+1}"
    #         self.producer.send(topic, message.encode())
    #     self.producer.flush()

    #     print(f"{num_messages} messages sent to topic {topic}")
