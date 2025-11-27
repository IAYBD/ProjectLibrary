from classes import Book
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


def list_books():
    books = load_books(FILE_PATH)
    print(f"\n=============Listado de libros===================")
    for book in books:
        print(book)
    print("================================\n")

def validate_data(data, instance):
    while not isinstance(data, instance):
        data = input(f"Tipo de dato inválido. Ingrese un valor de tipo {instance.__name__}: ")

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