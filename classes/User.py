class User:
    """Clase Usuario"""
    def __init__(self, id_user, name, surname, dni, email, phone, address, age):

        self.id_user = int(id_user)
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
    
    @classmethod
    def to_dict(cls, user):
        """Método para convertir un objeto en diccionario"""
        return {
            'id_user': user.id_user,
            'name': user.name,
            'surname': user.surname ,
            'dni': user.dni ,
            'email': user.email ,
            'phone': user.phone ,
            'address': user.address ,
            'age': user.age
        }

    @classmethod
    def from_dict(cls, data_dict):
        """Método para transformar un diccionario en un objeto"""
        return cls(**data_dict)