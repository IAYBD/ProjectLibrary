import csv
from classes import Book

class BookRepository:

    FILE_PATH = "data/biblioLibros.csv"
    FIELDS = ['id_book', 'title', 'author', 'year', 'page_num', 'gender', 'editorial', 'state', 'available']

    @classmethod
    def load_data(cls):
        data = []

        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for line in reader:
                b = Book.from_dict(line)
                data.append(b)

        return data
    
    @classmethod
    def find_a_book(cls, id):

        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            for line in reader:
                if int(line['id_book']) == id:
                    finded_book = Book(
                        id_book=int(line['id_book']),
                        title=line['title'],
                        author=line['author'],
                        year=line['year'],
                        page_num=line['page_num'],
                        gender=line['gender'],
                        editorial=line['editorial'],
                        state=line['state'],
                        available=line['available']
                    )
                    return finded_book

            return None

    @classmethod
    def get_max_id(cls):

        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')

            data = []

            for line in reader:
                data.append(int(line['id_book']))

        return max(data) if data else 0

    @classmethod
    def add_book(cls, b):
        with open(cls.FILE_PATH, "a", encoding="utf-8", newline='\n') as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow([
                b.id_book,
                b.title,
                b.author,
                b.year,
                b.page_num,
                b.gender,
                b.editorial,
                b.state,
                b.available
            ])

        return True

    @classmethod
    def rewrite(cls, data):
        with open(cls.FILE_PATH, "w", encoding="utf-8", newline="\n") as file:
            writer = csv.writer(file, delimiter=';')
            writer.writerow(cls.FIELDS)
            writer.writerows([Book.to_dict(b).values() for b in data])

    
    @classmethod
    def load_free_books(cls):
        data = []

        with open(cls.FILE_PATH, "rt", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=';')
            
            for line in reader:
                isAvailable = line['available'].strip().lower() == "true"
                if isAvailable:
                    b = Book.from_dict(line)
                    data.append(b)

        return data