class ClassTest:
    def instance_method(self):
        print(f'called instance_medthod of {self}')

    @classmethod
    def class_method(cls):
        print(f'called class_medthod of {cls}')

    @staticmethod
    def static_method():
        print('static_method')

test = ClassTest()
test.instance_method()

ClassTest.class_method()
ClassTest.static_method()


class Book:
    TYPES = ['hardcover', 'paperback']
    def __init__(self, name: str, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self) -> str:
        return f'<Book {self.name}>'

    @classmethod
    def hardcover(cls, name, page_weight) -> 'Book':
        return cls(name, cls.TYPES[0], page_weight +100)

book = Book.hardcover('Harry Potter', 1500)
print(book.book_type)
