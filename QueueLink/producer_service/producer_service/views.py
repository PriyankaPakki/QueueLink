from django.http import JsonResponse

# from producer_service.kafka_scripts.producer import KafkaMessageProducer
from kafka import KafkaProducer


class KafkaMessageProducer:
    def __init__(self, bootstrap_servers="kafka:9092"):
        self.producer = KafkaProducer(bootstrap_servers=bootstrap_servers)

    def produce_messages(self, topic, num_messages):
        for i in range(num_messages):
            message = f"Message {i+1}"
            self.producer.send(topic, message.encode())
        self.producer.flush()

        print(f"{num_messages} messages sent to topic {topic}")


def produce_bulk_messages(request):
    kafka_producer = KafkaMessageProducer(bootstrap_servers="kafka:9092")

    topic = "Q1"
    num_messages = 1000
    kafka_producer.produce_messages(topic, num_messages)

    return JsonResponse({"status": "success", "message": "1000 messages sent to Q1"})
