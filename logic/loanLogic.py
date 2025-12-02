from classes import Loan
from repo import LoanRepository, BookRepository, UserRepository
from datetime import date, timedelta

def askInteger(message):
    option = ""

    while not isinstance(option, int):
        try:
            option = int(input(message))
        except ValueError:
            continue

    return option


def idInList(id, list, field):

    for item in list:
        item_class = type(item)
        if item_class.to_dict(item)[field] == id:
            return True
    return False


def load_loans():
    loans = LoanRepository.load_data()

    for l in loans:
        print(l)


def register_loan():
    books = BookRepository.load_free_books()
    users = UserRepository.load_data()


    print("¿Qué Libro desea tomar prestado?\n")
    for b in books:
        print(b)

    book_option = askInteger("Ingrese el ID del libro que desea tomar prestado: ")

    if not idInList(book_option, list=books, field="id_book"):
        print("El ID del libro no es válido. Abortando operación.")
        return
    
    print("\n¿Quién tomará el libro prestado?\n")

    for u in users:
        print(u)

    user_option = askInteger("Ingrese el ID del usuario que quiere tomar prestado el libro: ")

    if not idInList(user_option, list=users, field="id_user"):
        print("El ID del usuario no es válido. Abortando operación.")
        return

    current_date = date.today()
    end_date = current_date + timedelta(days=7)

    loan = Loan(
        loan_id=LoanRepository.get_max_id() + 1,
        user_id=user_option,
        book_id=book_option,
        start_date=current_date,
        end_date=end_date,
        returning_date="None"
    )

    success = LoanRepository.register_loan(loan)

    if success:
        print("Préstamo registrado. Debe devolver el libro antes de:", end_date)

    book = BookRepository.find_a_book(book_option)

    all_books = BookRepository.load_data()

    index = all_books.index(book)
    book.available = False
    all_books[index] = book
    
    BookRepository.rewrite(all_books)