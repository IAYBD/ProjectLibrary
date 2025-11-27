from classes import *

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
    menu()
    option = input("Seleccione una opción: ")