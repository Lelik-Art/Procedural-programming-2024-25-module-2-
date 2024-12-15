"""
Написать класс Book, конструктор которого будет инициализировать следующие атрибуты:
id - идентификатор книги (целое число)
name - Название книги
pages - Количество страниц в книге
 Hint 
В классе должен быть объявлен метод __str__.

Метод __str__ должен возвращать строку формата

Книга "название_книги"

где "название_книги" берется с помощью атрибута name.

В классе должен быть объявлен метод __repr__.

Метод __repr__ должен возвращать валидную python строку, по которой можно инициализировать точно такой же экземпляр:

"Book(id_=1, name='test_name_1', pages=200)"
"""
BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book():
    def __init__(self, id_: int, name: str, pages: int):
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        return f'Book(id_ = {self.id}, name={self.name!r}, pages = {self.pages})'


if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
