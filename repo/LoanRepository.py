from classes import Loan
import csv

class LoanRepository:

    FIELDS = ["loan_id", "user_id", "book_id", "start_date", "end_date", "returning_date"]
    FILE_PATH = "data/biblioPrestamos.csv"

    @classmethod
    def load_data(cls):

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
    def get_max_id(cls):

        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            data = []

            for line in reader:
                data.append(int(line['loan_id']))

        return max(data) if data else 0

    @classmethod
    def register_loan(cls, loan):

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