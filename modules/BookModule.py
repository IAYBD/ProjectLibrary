from logic import load_books, list_books, add_book, getMaxId, remove_book, modify_book

def book_menu():
    """Menú de la parte de gestión de libros"""
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
    """Función para gestionar las operaciones relacionadas con los libros"""

    back = False
    while not back:
        book_menu()
        book_option = input("Seleccione una opción: ")

        match book_option:
            case "1":
                success = add_book()

                if success:
                    print("Libro añadido correctamente.")

            case "2":
                # Esto debería haberlo hecho en una función, pero se me olvidó
                book_id = ""
                while not isinstance(book_id, int):
                    try:
                        book_id = int(input("Ingrese el ID del libro a eliminar: "))
                        
                    except ValueError:
                       continue
                remove_book(book_id)
                    
            case "3":
                # Pedimos el id del libro a modificar
                book_id = ""
                while not isinstance(book_id, int):
                    try:
                        book_id = int(input("Ingrese el ID del libro a modificar: "))
                        
                    except ValueError:
                       continue
                modified_book = modify_book(book_id)

                if modified_book:
                    print(modified_book)
                
            case "4":
                list_books()
            case "5":
                back = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")