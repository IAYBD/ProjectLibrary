import csv
from classes import User

class UserRepository:

    """Clase que controla el acceso a la información guardada en el fichero"""

    FILE_PATH = "data/biblioUsuarios.csv"
    FIELDS = ["id_user","name","surname","dni","email","phone","address","age"]

    @classmethod
    def load_data(cls):
        """Carga de datos del fichero CSV, conversión a objetos User y retorno de lista de usuarios"""
        data = []

        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for line in reader:
                b = User.from_dict(line)

                data.append(b)

        return data
    
    @classmethod
    def find_a_user(cls, id):
        """Método que carga todos los usuarios y devuelve el usuario con el ID dado si lo encuentra o None en caso contrario"""
        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            for line in reader:
                if int(line['id_user']) == id:
                    finded_user = User(
                        id_user=int(line['id_user']),
                        name=line['name'],
                        surname=line['surname'],
                        dni=line['dni'],
                        email=line['email'],
                        phone=line['phone'],
                        address=line['address'],
                        age=line['age']
                    )
                    return finded_user


        return None

    @classmethod
    def get_max_id(cls):
        """Método que obtiene el ID más alto y lo devuelve"""
        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            data = []
            for line in reader:
                b = User(
                    id_user=int(line['id_user']),
                    name=line['name'],
                    surname=line['surname'],
                    dni=line['dni'],
                    email=line['email'],
                    phone=line['phone'],
                    address=line['address'],
                    age=line['age']
                )

                data.append(b)

        data.sort(key=lambda user: user.id_user, reverse=True)

        return data[0].id_user if data else 0

    @classmethod
    def add_user(cls, user):
        """Método que recibe un usuario y lo añade al final del fichero"""
        try:
            with open(cls.FILE_PATH, "a", encoding="utf-8", newline="\n") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow([user.id_user, user.name, user.surname, user.dni, user.email, user.phone, user.address, user.age])
        except Exception as e:
            print(f"Error al añadir el usuario: {e}")
            return False
        
        return True

    @classmethod
    def rewrite(cls, data):
        """Método que recibe una lista de usuarios y la sobreescribe al contenido del fichero"""
        try:

            with open(cls.FILE_PATH, "w", encoding="utf-8", newline="") as file:
                writer = csv.writer(file, delimiter=';')
                writer.writerow(cls.FIELDS)
                writer.writerows([vars(user).values() for user in data])
        except Exception as e:
            print(f"Error al reescribir el fichero: {e}")
            return False

        return True

