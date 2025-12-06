# Import Zone
from modules import manage_books, manage_users
from logic.loanLogic import *

def menu():
    """
    Menú principal de la aplicación
    """
    print("================================")
    print("Bienvenido al sistema de gestión de la biblioteca")
    print("Para salir del programa, presione 6 ó Ctrl+C")
    print("================================")
    print("1. Gestión de Libros")
    print("2. Gestión de Usuarios")
    print("3. Registro de Préstamos")
    print("4. Registro de Devoluciones")
    print("5. Listado de Préstamos")
    print("6. Salir")


# Variable que controla la finalización del programa
finished = False


# Bucle principal
while not finished:

    # Try-Except creado para capturar la interrupción del programa con Ctrl+C
    # (Innecesario tal vez, pero útil durante el desarrollo y pruebas para terminar el programa)
    try:

        # Llamada del menú
        menu()

        # Solicitud de opción al usuario
        option = input("Seleccione una opción: ")


        # Procesamiento de la opción
        match option:
            case "1":
                manage_books()
            case "2":
                manage_users()
            case "3":
                register_loan()
            case "4":
                register_devolutions()
            case "5":
                load_loans()
            case "6":
                print("Saliendo del sistema...")
                finished = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")

    except KeyboardInterrupt:
        print("\nSaliendo del sistema...")
        finished = True
    