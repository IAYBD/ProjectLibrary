from logic.userLogic import *

def user_menu():
    """Menú de gestión de usuarios"""
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
    """Función que controla la parte de gestión de usuarios"""
    back = False
    while not back:
        user_menu()
        user_option = input("Seleccione una opción: ")

        match user_option:
            case "1":
                success = add_user()
                if success:
                    print("Usuario añadido correctamente.")
                else:
                    print("No se pudo añadir el usuario.")
            case "2":
                user_id = int(input("Ingrese el ID del usuario a eliminar: "))
                success = delete_user(user_id)
                if success:
                    print("Usuario eliminado correctamente.")
                else:
                    print("No se pudo eliminar el usuario.")
            case "3":
                success = edit_user()
                if success:
                    print("Usuario modificado correctamente.")
                else:
                    print("No se pudo modificar el usuario.")
            case "4":
                print("\n=============Listado de usuarios===================")
                users = load_users()
                for user in users:
                    print(user)
            case "5":
                back = True
            case _:
                print("Opción no válida. Por favor, intente de nuevo.")