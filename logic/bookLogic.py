from classes import Book
from repo import BookRepository

def load_books():
    """Función para cargar los libros desde el fichero"""
    return BookRepository.load_data()

def getMaxId():
    """Función para obtener el id más alto registrado.
    Importante para calcular el ID de los nuevos elementos"""
    return BookRepository.get_max_id()


def list_books():
    """Función para mostrar una lista de libros"""
    books = load_books()
    print(f"\n=============Listado de libros===================")
    for book in books:
        print(book)
    print("================================\n")

def validate_data(data, instance):
    """Esta función la creé para forzar que el usuario introdujese un valor del tipo que yo quería.
    Sin embargo como no me parecía una experiencia de usuario muy agradable para tipos como Boolean, creé otra función
    y dejé esta para los enteros"""
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

def assign_specific_values(message, value1, value2):
    """Esta es la función que mencioné anteriormente. Como hay 2 campos que tienen valores determinados decidí crear este método
    donde fuerzo al usuario a que elija el valor introduciendo 1 o 2"""
    option = ""

    while not isinstance(option, int):
        try:
            option = int(input(message))

        except ValueError:
            continue

    match option:

        case 1:
            option = value1

        case 2: 
            option = value2

    return option

def add_book():
    """Función para añadir un nuevo libro.
    Se encarga de solicitar los datos al usuario, crear el objeto y escribir una nueva línea en el csv
    """

    # Solicitamos los datos
    title = input("Ingrese el título del libro: ")
    author = input("Ingrese el autor del libro: ")
    year = validate_data(input("Ingrese el año de publicación: "), int)
    page_num = validate_data(input("Ingrese el número de páginas: "), int)
    gender = input("Ingrese el género del libro: ")
    editorial = input("Ingrese la editorial del libro: ")
    state = assign_specific_values("Ingrese el estado del libro (1 para Nuevo y 2 para Usado): ", "Nuevo", "Usado")
    available = assign_specific_values("¿El libro está disponible? (1 para verdadero y 2 para falso): ", True, False)
    
    # Creamos el objeto libro
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

    # Añadimos al repositorio
    success = BookRepository.add_book(b)

    # Devolvemos si la operación ha sido exitosa o no
    return success

def remove_book(book_id):
    """Función para eliminar un libro del sistema"""
    books = load_books()
    book_for_remove = BookRepository.find_a_book(book_id)
    books.remove(book_for_remove)
    
    BookRepository.rewrite(books)

def modify_book(book_id):
    """Función para modificar un libro del sistema"""
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