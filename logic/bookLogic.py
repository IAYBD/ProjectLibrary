from classes import Book
from repo import BookRepository
from .normalise import normalize
import csv

FILE_PATH = "data/biblioLibros.csv"


def load_books():
    return BookRepository.load_data()

def getMaxId():
    return BookRepository.get_max_id()


def list_books():
    books = load_books()
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

def add_book():
    title = input("Ingrese el título del libro: ")
    author = input("Ingrese el autor del libro: ")
    year = validate_data(input("Ingrese el año de publicación: "), int)
    page_num = validate_data(input("Ingrese el número de páginas: "), int)
    gender = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    state = input("Ingrese el estado del libro (Nuevo/Usado): ")
    available = input("¿El libro está disponible? (True/False): ")

    b = Book(
        id_book=getMaxId() + 1,
        title=title,
        author=author,
        year=year,
        page_num=page_num,
        gender=gender,
        editorial=editorial,
        state=state,
        available=available
    )

    success = BookRepository.add_book(b)

    return success

def remove_book(book_id):
    books = load_books()
    book_for_remove = BookRepository.find_a_book(book_id)
    books.remove(book_for_remove)
    
    BookRepository.rewrite(books)

def modify_book(book_id):

    books = load_books()
    book = BookRepository.find_a_book(book_id)

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

    BookRepository.rewrite(books)

    return f"Libro modificado: {b}"