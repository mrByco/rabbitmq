import pika
import os
from dotenv import load_dotenv

load_dotenv()

counter = 0
rabbitmq_host = os.getenv("RABBITMQ_HOST", "localhost")
color_filter = os.getenv("COLOR")

def callback(ch, method, properties, body):
    global counter
    message_color = body.decode()
    if message_color == color_filter:
        counter += 1
        print(f"{color_filter} received ({counter})")
        if counter == 10:
            channel.basic_publish(exchange='',
                                  routing_key='colorStatistics',
                                  body=f"10 {color_filter} messages have been processed")
            counter = 0

connection = pika.BlockingConnection(pika.ConnectionParameters(rabbitmq_host))
channel = connection.channel()

channel.queue_declare(queue='colorQueue')
channel.queue_declare(queue='colorStatistics')

channel.basic_consume(queue='colorQueue',

                      on_message_callback=callback,
                      auto_ack=True)

print(f"Waiting for {color_filter} messages...")
channel.start_consuming()
