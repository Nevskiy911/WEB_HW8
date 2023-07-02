from mongoengine import Document, StringField, DateTimeField, ReferenceField, ListField


class Author(Document):
    name = StringField(required=True)
    date_of_birth = DateTimeField()
    place_of_birth = StringField()
    biography = StringField()


class Quote(Document):
    author = ReferenceField(Author)
    text = StringField(required=True)
    tags = ListField(StringField())
