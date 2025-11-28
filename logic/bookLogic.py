from classes import Book
from .normalise import normalize
import csv

FILE_PATH = "data/biblioLibros.csv"


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

def getMaxId(file_path):
    with open(file_path, "rt", encoding="utf-8") as file:
        reader = csv.DictReader(file, delimiter=';')
        max_id = 0
        for line in reader:
            current_id = int(line['id_book'])
            if current_id > max_id:
                max_id = current_id
        return max_id

def locate_book(book_name):
    books = load_books(FILE_PATH)
    for book in books:
        if normalize(book.title) == normalize(book_name):
            return book
    return None

def rewrite(fields, data):
    with open(FILE_PATH, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(fields)
        writer.writerows([vars(book).values() for book in data])

def list_books():
    books = load_books(FILE_PATH)
    print(f"\n=============Listado de libros===================")
    for book in books:
        print(book)
    print("================================\n")

def validate_data(data, instance):

    try:
        data = instance(data)
    except ValueError:
        while not isinstance(data, instance):
            data = input(f"Tipo de dato inválido. Ingrese un valor de tipo {instance.__name__}: ")
            try:
                data = instance(data)
            except ValueError:
                continue

    return data

def add_book(file_path):
    title = input("Ingrese el título del libro: ")
    author = input("Ingrese el autor del libro: ")
    year = validate_data(input("Ingrese el año de publicación: "), int)
    page_num = validate_data(input("Ingrese el número de páginas: "), int)
    gender = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    state = input("Ingrese el estado del libro (Nuevo/Usado): ")
    available = input("¿El libro está disponible? (True/False): ")

    b = Book(
        id_book=getMaxId(file_path) + 1,
        title=title,
        author=author,
        year=year,
        page_num=page_num,
        gender=gender,
        editorial=editorial,
        state=state,
        available=available
    )

    with open(file_path, "a", encoding="utf-8", newline='\n') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            b.id_book,
            b.title,
            b.author,
            b.year,
            b.page_num,
            b.gender,
            b.editorial,
            b.state,
            b.available
        ])

def remove_book(book_name, file_path):
    books = load_books(file_path)
    book_for_remove = locate_book(book_name)
    books.remove(book_for_remove)
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['id_book', 'title', 'author', 'year', 'page_num', 'gender', 'editorial', 'state', 'available'])
        writer.writerows([vars(book).values() for book in books])

def modify_book(book_name):

    books = load_books(FILE_PATH)
    book = locate_book(book_name)

    if not book:
        print("Libro no encontrado.")
        return
    
    title = input("Ingrese el título del libro: ")
    author = input("Ingrese el autor del libro: ")
    year = validate_data(input("Ingrese el año de publicación: "), int)
    page_num = validate_data(input("Ingrese el número de páginas: "), int)
    gender = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    state = input("Ingrese el estado del libro (Nuevo/Usado): ")
    available = input("¿El libro está disponible? (True/False): ")

    b = Book(
        id_book=book.id_book,
        title=title,
        author=author,
        year=year,
        page_num=page_num,
        gender=gender,
        editorial=editorial,
        state=state,
        available=available
    )

    index = books.index(book)
    books[index] = b

    rewrite(['id_book', 'title', 'author', 'year', 'page_num', 'gender', 'editorial', 'state', 'available'], books)

    return f"Libro modificado: {b}"