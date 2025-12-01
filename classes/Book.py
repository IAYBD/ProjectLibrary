class Book:

    def __init__(self, id_book, title, author, year, page_num, gender, editorial, state, available):

        self.id_book = int(id_book)
        self.title = title
        self.author = author
        self.year = year
        self.page_num = page_num
        self.gender = gender
        self.editorial = editorial
        self.state = state
        self.available = available

    def __eq__(self, value):
        if not isinstance(value, Book):
            return False
        return self.id_book == value.id_book

    def __str__(self):
        return f"ID: {self.id_book} | Title: {self.title} | Author: {self.author} | Year: {self.year} | Pages: {self.page_num} | Gender: {self.gender} | Editorial: {self.editorial} | State: {self.state} | Available: {self.available}"
    

    @classmethod
    def to_dict(cls, book):
        return {
            'id_book': book.id_book,
            'title': book.title ,
            'author': book.author ,
            'year': book.year ,
            'page_num': book.page_num ,
            'gender': book.gender ,
            'editorial': book.editorial ,
            'state': book.state ,
            'available': book.available
        }

    @classmethod
    def from_dict(cls, data_dict):
       return cls(**data_dict) 