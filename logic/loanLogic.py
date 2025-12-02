from repo import LoanRepository, BookRepository, UserRepository
from datetime import date

def available_books():

    books = BookRepository.load_free_books()

    

def register_loan():
    books = BookRepository.load_free_books()
    users = UserRepository.load_data()

    for b in books:
        print(b)

    option = ""

    while not isinstance(option, int):
        try:
            option = input("Ingrese el ID del libro que desea tomar prestado: ")
        except ValueError:
            continue