import json
from mongoengine import connect
from models import Author, Quote


def load_authors():
    with open('authors.json', 'r', encoding='utf-8') as file:
        authors_data = json.load(file)

    for author_data in authors_data:
        author = Author(
            name=author_data['fullname'],
            date_of_birth=author_data['born_date'],
            place_of_birth=author_data['born_location'],
            biography=author_data['description']
        )
        author.save()


def load_quotes():
    with open('quotes.json', 'r', encoding='utf-8') as file:
        quotes_data = json.load(file)

    for quote_data in quotes_data:
        author = Author.objects(name=quote_data['author']).first()

        quote = Quote(
            author=author,
            text=quote_data['quote'],
            tags=quote_data['tags']
        )
        quote.save()

if __name__ == '__main__':
    connect('WEB', host='mongodb+srv://Nevskiy911:MAleXX322537@nevskiy911.fyrqia2.mongodb.net/')
    load_authors()
    load_quotes()
