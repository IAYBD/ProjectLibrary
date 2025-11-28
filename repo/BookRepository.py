import csv
from classes import Book

class BookRepository:

    FILE_PATH = "data/biblioLibros.csv"
    FIELDS = ['id_book', 'title', 'author', 'year', 'page_num', 'gender', 'editorial', 'state', 'available']

    def load_data(self):
        data = []

        with open(self.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for line in reader:
                b = Book(
                    id_book=line['id_book'],
                    title=line['title'],
                    author=line['author'],
                    year=int(line['year']),
                    page_num=int(line['page_num']),
                    gender=line['gender'],
                    editorial=line['editorial'],
                    state=line['state'],
                    available=line['available']
                )

                data.append(b)

        return data
    
    def rewrite(fields, data):
        with open(BookRepository.FILE_PATH, "w", encoding="utf-8", newline="") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(fields)
            writer.writerows([vars(book).values() for book in data])