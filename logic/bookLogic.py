from classes import Book
import csv


def load_books(file_path):

    data = []

    with open(file_path, "rt", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        
        for line in reader:
            b = Book(
                id_book=line['id_book'],
                title=line['title'],
                author=line['author'],
                year=int(line['year']),
                page_num=int(line['page_num']),
                gender=line['gender'],
                editorial=line['editorial'],
                state=line['state'],
                available=line['available']
            )

            data.append(b)

    return data


def list_books():
    books = load_books("data/biblioLibros.csv")
    for book in books:
        print(book)