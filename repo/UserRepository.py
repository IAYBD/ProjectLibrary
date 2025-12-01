import csv
from classes import User

class UserRepository:

    FILE_PATH = "data/biblioUsuarios.csv"
    FIELDS = ["id_user","name","surname","dni","email","phone","address","age"]

    """Carga de datos del fichero CSV, conversión a objetos User y retorno de lista de usuarios"""
    @classmethod
    def load_data(cls):
        data = []

        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for line in reader:
                b = User.from_dict(line)

                data.append(b)

        return data
    
    @classmethod
    def find_a_user(cls, id):

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
        with open(cls.FILE_PATH, "a", encoding="utf-8", newline="\n") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([user.id_user, user.name, user.surname, user.dni, user.email, user.phone, user.address, user.age])

    @classmethod
    def rewrite(cls, data):
        with open(cls.FILE_PATH, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(cls.FIELDS)
            writer.writerows([vars(book).values() for book in data])

