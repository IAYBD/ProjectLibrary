from classes import Loan
import csv

class LoanRepository:

    FIELDS = ["loan_id", "user_id", "book_id", "start_date", "end_date", "returning_date"]
    FILE_PATH = "data/biblioPrestamos.csv"

    @classmethod
    def load_data(cls):
        """Método que carga todos los préstamos"""
        try:
            data = []

            with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=';')

                for line in reader:
                    loan = Loan.from_dict(line)
                    data.append(loan)

            return data
        
        except FileNotFoundError:
            print("Archivo no encontrado.")

    @classmethod
    def load_unfinished_loans(cls):
        """Método que carga todos los préstamos y devuelve los que están aún vigentes"""
        try:
            data = []

            with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
                reader = csv.DictReader(file, delimiter=';')

                for line in reader:
                    if line['returning_date'] == "None":
                        loan = Loan.from_dict(line)
                        data.append(loan)

            return data
        
        except FileNotFoundError:
            print("Archivo no encontrado.")

    @classmethod
    def get_max_id(cls):
        """Método que obtiene el ID más alto y lo devuelve"""
        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            data = []

            for line in reader:
                data.append(int(line['loan_id']))

        return max(data) if data else 0

    @classmethod
    def register_loan(cls, loan):
        """Método que recibe un préstamo y lo añade al final del fichero"""
        with open(cls.FILE_PATH, "a", encoding="utf-8", newline='\n') as file:
            writer = csv.DictWriter(file, fieldnames=cls.FIELDS, delimiter=';')
            writer.writerow({
                'loan_id': loan.loan_id,
                'user_id': loan.user_id,
                'book_id': loan.book_id,
                'start_date': loan.start_date,
                'end_date': loan.end_date,
                'returning_date': loan.returning_date
            })

        return True
    
    @classmethod
    def rewrite(cls, data):
        """Método que recibe una lista de préstamos y la sobreescribe al contenido del fichero"""
        with open(cls.FILE_PATH, "w", encoding="utf-8", newline="\n") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(cls.FIELDS)
            writer.writerows([Loan.to_dict(l).values() for l in data])