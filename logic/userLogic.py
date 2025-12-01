from classes import User
from repo import UserRepository
import re

phone_validations = r"\d{9}"
dni_validations = r"^\d{8}[A-Za-z]$"
email_validations = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

def load_users():
    return UserRepository().load_data()


def validate_regex(value, pattern):
    valid = False
    if not re.match(pattern, value):
        while not valid:
            value = input(f"El valor '{value}' no es válido. Por favor, ingrese un valor correcto: ")
            if re.match(pattern, value):
                valid = True
    
    return value

def validateIsANumber(value):
    try:
        value = int(value)
    except ValueError:
        while not isinstance(value, int):
            value = input("Tipo de dato inválido. Ingrese un valor numérico: ")
            try:
                value = int(value)
            except ValueError:
                continue

    return value

def add_user():
    name = input("Ingrese el nombre del usuario: ")
    surname = input("Ingrese el apellido del usuario: ")
    dni = validate_regex(input("Ingrese el DNI del usuario: "), dni_validations)
    email = validate_regex(input("Ingrese el email del usuario: "), email_validations)
    phone = validate_regex(input("Ingrese el teléfono del usuario: "), phone_validations)
    address = input("Ingrese la dirección del usuario: ")
    age = validateIsANumber(input("Ingrese la edad del usuario: "))

    u = User(
        id_user=UserRepository.get_max_id() + 1,
        name=name,
        surname=surname,
        dni=dni,
        email=email,
        phone=phone,
        address=address,
        age=age
    )

    UserRepository.add_user(u)

def edit_user():

    users = load_users()

    user_id = validateIsANumber(input("Ingrese el ID del usuario a modificar: "))
    name = input("Ingrese el nombre del usuario: ")
    surname = input("Ingrese el apellido del usuario: ")
    dni = validate_regex(input("Ingrese el DNI del usuario: "), dni_validations)
    email = validate_regex(input("Ingrese el email del usuario: "), email_validations)
    phone = validate_regex(input("Ingrese el teléfono del usuario: "), phone_validations)
    address = input("Ingrese la dirección del usuario: ")
    age = validateIsANumber(input("Ingrese la edad del usuario: "))

    u = User(
        id_user=user_id,
        name=name,
        surname=surname,
        dni=dni,
        email=email,
        phone=phone,
        address=address,
        age=age
    )

    finded_user = UserRepository.find_a_user(user_id)

    if not finded_user:
        print("No se ha encontrado ningún usuario con ese ID.")
        return

    print(finded_user)

    index = users.index(finded_user)
    users[index] = u

    UserRepository.rewrite(users)
    return True

def delete_user(user_id):

    users = load_users()
    users = list(filter(lambda u: u.id_user != user_id, users))

    UserRepository.rewrite(users)