from models import Contact
import pika


NUM_CONTACTS = 10


credentials = pika.PlainCredentials(
    'mkkuhwvi', 'S5m0YoJ941_3_T9DMKWVupk8Cbtv14zd')
connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
channel = connection.channel()

channel.queue_declare(queue='contact_queue')


for i in range(NUM_CONTACTS):
    contact = Contact(
        full_name=f'Contact {i}', email=f'contact{i}@example.com')
    contact.save()

    channel.basic_publish(
        exchange='', routing_key='contact_queue', body=str(contact.id))

    print(f'Contact {contact.id} sent to RabbitMQ')

connection.close()
