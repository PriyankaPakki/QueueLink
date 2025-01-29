from kafka.admin import KafkaAdminClient, NewTopic
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Create Kafka topics"

    def handle(self, *args, **kwargs):
        # kafka configuration

        BOOTSTRAP_SERVERS = "kafka:9092"

        # Define topics

        topics = [
            NewTopic(name="Q1", num_partitions=2, replication_factor=1),
            # NewTopic(name="Q2", num_partitions=1, replication_factor=1),
        ]

        # Create KafkaAdminClient
        admin_client = KafkaAdminClient(
            bootstrap_servers=BOOTSTRAP_SERVERS, client_id="admin-client"
        )

        # Create topics
        try:
            admin_client.create_topics(new_topics=topics, validate_only=False)
            self.stdout.write(self.style.SUCCESS("Topics Q1 created successfully!"))
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"Error creating topics: {e}"))
        finally:
            admin_client.close()
