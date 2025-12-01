from logic.userLogic import *

def user_menu():
    print("================================")
    print("Ha seleccionado la opción de 'Gestión de Usuarios'")
    print("¿Qué desea hacer?")
    print("================================\n")
    print("1. Alta de un usuario")
    print("2. Baja de un usuario")
    print("3. Modificación de un usuario")
    print("4. Listado de usuarios")
    print("5. Volver atrás")


def manage_users():

    back = False
    while not back:
        user_menu()
        user_option = input("Seleccione una opción: ")

        match user_option:
            case "1":
                pass  # Lógica para agregar un usuario
            case "2":
                pass  # Lógica para eliminar un usuario
            case "3":
                pass  # Lógica para modificar un usuario
            case "4":
                print("\n=============Listado de usuarios===================")
                users = load_users()
                for user in users:
                    print(user)
            case "5":
                back = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")