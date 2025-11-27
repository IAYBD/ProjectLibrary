class Loan:

    _loan_id = 1

    def __init__(self, user_id, book_id, start_date, end_date, returning_date):
        self.loan_id = Loan._loan_id
        Loan._loan_id += 1
        self.user_id = user_id
        self.book_id = book_id
        self.start_date = start_date
        self.end_date = end_date
        self.returning_date = returning_date