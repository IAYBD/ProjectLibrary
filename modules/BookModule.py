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
                success = add_book()

                if success:
                    print("Libro añadido correctamente.")

            case "2":
                book_id = ""
                while not isinstance(book_id, int):
                    try:
                        book_id = int(input("Ingrese el ID del libro a eliminar: "))
                        
                    except ValueError:
                       continue
                remove_book(book_id)
                    
            case "3":
                book_id = input("Ingrese el ID del libro a modificar: ")
                modified_book = modify_book(int(book_id))
                print(modified_book)
                
            case "4":
                list_books()
            case "5":
                back = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")