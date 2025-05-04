import pika
import random
import time
import os
from dotenv import load_dotenv

load_dotenv()

rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue='colorQueue')

colors = ['RED', 'GREEN', 'BLUE']

while True:
    color = random.choice(colors)
    channel.basic_publish(exchange='',
                          routing_key='colorQueue',
                          body=color)
    print(f"Sent: {color}")
    time.sleep(1)
