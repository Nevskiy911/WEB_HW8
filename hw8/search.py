from mongoengine import connect
from models import Author, Quote


def search_quotes(query):
    query_type, query_value = query.split(':')

    connect('WEB', host='mongodb+srv://Nevskiy911:MAleXX322537@nevskiy911.fyrqia2.mongodb.net/')

    if query_type == 'name':
        author = Author.objects(name=query_value).first()
        if author:
            quotes = Quote.objects(author=author)
            for quote in quotes:
                print(quote.text)
        else:
            print('Автор не знайдений.')
    elif query_type == 'tag':
        quotes = Quote.objects(tags=query_value)
        for quote in quotes:
            print(quote.text)
    elif query_type == 'tags':
        tags = query_value.split(',')
        quotes = Quote.objects(tags__in=tags)
        for quote in quotes:
            print(quote.text)
    else:
        print('Невірний формат запиту.')


if __name__ == '__main__':
    while True:
        print("Для виходу з програми напишіть exit")
        user_input = input('Введіть команду (наприклад: name:John; tag:smile або tags:world):--->>> ')
        if user_input == 'exit':
            break
        search_quotes(user_input)
