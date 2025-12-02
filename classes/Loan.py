class Loan:

    def __init__(self, loan_id, user_id, book_id, start_date, end_date, returning_date):
        self.loan_id = loan_id
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = start_date
        self.end_date = end_date
        self.returning_date = returning_date


    @classmethod
    def from_dict(cls, data_dict):
        return cls(**data_dict)