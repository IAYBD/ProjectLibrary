class User:

    def __init__(self, id_user, name, surname, dni, email, phone, address, age):

        self.id_user = id_user
        self.name = name
        self.surname = surname
        self.dni = dni
        self.email = email
        self.phone = phone
        self.address = address
        self.age = age

    def __eq__(self, value):

        if not isinstance(value, User):
            return False
        
        return self.id_user == value.id_user

    def __str__(self):
        return f"ID: {self.id_user} | Name: {self.name} | Surname: {self.surname} | DNI: {self.dni} | Email: {self.email} | Phone: {self.phone} | Address: {self.address} | Age: {self.age}"