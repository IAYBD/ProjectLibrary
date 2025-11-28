from modules import manage_books

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

finished = False

while not finished:
    try:

        menu()
        option = input("Seleccione una opción: ")

        match option:
            case "1":
                manage_books()
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
    