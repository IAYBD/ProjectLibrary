from classes import *
from logic import load_books, list_books

def menu():
    print("================================")
    print("Bienvenido al sistema de gestión de la biblioteca")
    print("================================")
    print("1. Gestión de Libros")
    print("2. Gestión de Usuarios")
    print("3. Registro de Préstamos")
    print("4. Registro de Devoluciones")
    print("5. Listado de Préstamos")
    print("6. Salir")

def manage_books():
    print("================================")
    print("Ha seleccionado la opción de 'Gestión de Libros'")
    print("¿Qué desea hacer?")
    print("================================")
    print("1. Alta de un libro")
    print("2. Baja de un libro")
    print("3. Modificación de un libro")
    print("4. Listado de libros")
    print("5. Volver atrás")


finished = False

while not finished:
    try:

        menu()
        option = input("Seleccione una opción: ")

        match option:
            case "1":
                manage_books()
                list_books()
            case "2":
                print()
            case "3":
                print()
            case "4":
                print()
            case "5":
                print()
            case "6":
                print("Saliendo del sistema...")
                finished = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

    except KeyboardInterrupt:
        print("\nSaliendo del sistema...")
        finished = True
    