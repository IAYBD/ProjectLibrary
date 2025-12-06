from classes import Loan
from repo import LoanRepository, BookRepository, UserRepository
from datetime import date, timedelta

def askInteger(message):
    """Método que obliga al usuario a introducir un número entero"""
    option = ""

    while not isinstance(option, int):
        try:
            option = int(input(message))
        except ValueError:
            continue

    return option


def idInList(id, list, field):
    """Método que recorre una lista para averiguar si contiene un determinado ID"""
    for item in list:
        item_class = type(item)
        if item_class.to_dict(item)[field] == id:
            return True
    return False


def load_loans():
    """Método que carga los préstamos y los lista"""
    loans = LoanRepository.load_data()

    for l in loans:
        print(l)

def load_unfinished_loans():
    """Método que carga los préstamos vigentes y los lista"""
    loans = LoanRepository.load_unfinished_loans()

    print("¿Qué préstamo quiere finalizar?\n")

    for l in loans:
        print(l)

def register_loan():
    """Método para registrar un préstamo"""
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

def register_devolutions():
    """Método para registrar una devolución"""
    loans = LoanRepository.load_unfinished_loans()

    print("¿Qué préstamo quiere finalizar?\n")

    for l in loans:
        print(l)

    loan_option = askInteger("Ingrese el ID del préstamo que desea finalizar: ")

    if not idInList(loan_option, list=loans, field="loan_id"):
        print("El ID del préstamo no es válido. Abortando operación.")
        return

    loan = next((l for l in loans if l.loan_id == loan_option), None)

    loan.returning_date = date.today()

    all_loans = LoanRepository.load_data()

    index = all_loans.index(loan)
    all_loans[index] = loan

    LoanRepository.rewrite(all_loans)

    book = BookRepository.find_a_book(loan.book_id)

    if not book:
        print("No se ha encontrado el libro asociado al préstamo. Abortando operación.")
        return

    all_books = BookRepository.load_data()

    index = all_books.index(book)
    book.available = True
    all_books[index] = book
    
    BookRepository.rewrite(all_books)

    print("Préstamo finalizado. Gracias por devolver el libro.")