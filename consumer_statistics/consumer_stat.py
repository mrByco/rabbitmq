import pika
import os
from dotenv import load_dotenv

load_dotenv()

rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")

def callback(ch, method, properties, body):
    print(f"STATISTICS RECEIVED: {body.decode()}")

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue='colorStatistics')

channel.basic_consume(
    queue='colorStatistics',
    on_message_callback=callback,
    auto_ack=True
)

print(f"Listening for statistics messages on {rabbitmq_host}...")
channel.start_consuming()
