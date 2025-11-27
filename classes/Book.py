class Book:

    def __init__(self, id_book, title, author, year, page_num, gender, editorial, state, available):

        self.id_book = id_book
        self.title = title
        self.author = author
        self.year = year
        self.page_num = page_num
        self.gender = gender
        self.editorial = editorial
        self.state = state
        self.available = available

    def __str__(self):
        return f"ID: {self.id_book} | Title: {self.title} | Author: {self.author} | Year: {self.year} | Pages: {self.page_num} | Gender: {self.gender} | Editorial: {self.editorial} | State: {self.state} | Available: {self.available}"