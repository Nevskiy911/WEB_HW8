from mongoengine import Document, StringField, BooleanField, IntField


class Contact(Document):
    full_name = StringField(required=True)
    email = StringField(required=True)
    is_message_sent = BooleanField(default=False)
    age = IntField()
    phone = StringField()

    def send_message(self):
        pass

    def __str__(self):
        return f'Contact: {self.full_name} ({self.email})'
