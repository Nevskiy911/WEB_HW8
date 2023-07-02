import sys
from models import Contact
import pika


def main():
    credentials = pika.PlainCredentials(
        'mkkuhwvi', 'S5m0YoJ941_3_T9DMKWVupk8Cbtv14zd')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()
    channel.queue_declare(queue='contact_queue')


    def callback(ch, method, properties, body):
        contact_id = body.decode()
        contact = Contact.objects(id=contact_id).first()
        if contact:
            contact.send_email()
            contact.is_message_sent = True
            contact.save()
            print(f'Message sent to Contact {contact_id}')

    channel.basic_consume(queue='contact_queue',
                          on_message_callback=callback, auto_ack=True)

    print('Waiting for messages. To exit, press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
