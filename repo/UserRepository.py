import csv
from classes import User

class UserRepository:

    FILE_PATH = "data/biblioUsuarios.csv"
    FIELDS = ["id_user","name","surname","dni","email","phone","address","age"]

    """Carga de datos del fichero CSV, conversión a objetos User y retorno de lista de usuarios"""
    def load_data(self):
        data = []

        with open(self.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            
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

        return data
    
    def add_user(self, user):
        with open(self.FILE_PATH, "a", encoding="utf-8", newline="\n") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([user.id_user, user.name, user.surname, user.dni, user.email, user.phone, user.address, user.age])


    def rewrite(fields, data):
        with open(UserRepository.FILE_PATH, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(fields)
            writer.writerows([vars(book).values() for book in data])