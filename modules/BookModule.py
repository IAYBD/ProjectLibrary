from logic import load_books, list_books, add_book, getMaxId, remove_book, modify_book

def book_menu():
    print("================================")
    print("Ha seleccionado la opción de 'Gestión de Libros'")
    print("¿Qué desea hacer?")
    print("================================\n")
    print("1. Alta de un libro")
    print("2. Baja de un libro")
    print("3. Modificación de un libro")
    print("4. Listado de libros")
    print("5. Volver atrás")

def manage_books():

    back = False
    while not back:
        book_menu()
        book_option = input("Seleccione una opción: ")

        match book_option:
            case "1":
                add_book("data/biblioLibros.csv")
            case "2":
                book_id = int(input("Ingrese el ID del libro a eliminar: "))
                remove_book(book_id, "data/biblioLibros.csv")
            case "3":
                book_name = input("Ingrese el nombre del libro a modificar: ")
                modified_book = modify_book(book_name)
                print(modified_book)
            case "4":
                list_books()
            case "5":
                back = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")