from datetime import date
class Loan:

    def __init__(self, loan_id, user_id, book_id, start_date, end_date, returning_date):
        self.loan_id = loan_id
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = date.fromisoformat(start_date) if type(start_date) is str else start_date
        self.end_date = date.fromisoformat(end_date) if type(end_date) is str else end_date
        self.returning_date = returning_date

    def __str__(self):
        return f"Préstamo con ID: {self.loan_id}, al usuario {self.user_id} del libro con ID {self.book_id} desde {self.start_date} hasta {self.end_date}, Fecha de devolución: {self.returning_date}"

    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)