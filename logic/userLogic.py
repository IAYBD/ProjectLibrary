from repo import UserRepository

def load_users():
    return UserRepository().load_data()