"""
Написать класс Library, конструктор которого будет инициализировать следующие атрибуты:

books - Список книг
Конструктор должен принимать необязательный аргумент со значением по умолчанию. Если пользователь его не передал, 
то библиотека инициализируется с пустым списком книг.

В классе должен быть объявлен метод get_next_book_id.
Метод, возвращающий идентификатор для добавления новой книги в библиотеку.
Если книг в библиотеке нет, то вернуть 1.
Если книги есть, то вернуть идентификатор последней книги увеличенный на 1.

В классе должен быть объявлен метод get_index_by_book_id. Метод принимает в качестве аргумента целое число, 
являющееся валидным id книги (т. е. такое, каким можно проинициализировать экземпляр Book). 
Метод возвращает индекс книги в списке, который хранится в атрибуте экземпляра класса.
Если книга существует, то вернуть индекс из списка.
Если книги нет, то вызвать ошибку ValueError с сообщением: "Книги с запрашиваемым id не существует"
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


class Library():
    def __init__(self, books: list = []):
        self.books = books

    def get_next_book_id(self) -> int:
        if self.books == []:
            return 1
        else:
            result = self.books[-1].id + 1
            return result

    def get_index_by_book_id(self, id_: int) -> int:
        id_list = []
        for i in range(len(self.books)):
            id_list.append(self.books[i].id)
        for book in id_list:
            if id_ == book:
                return(book)
        else:
            raise ValueError("Книги с запрашиваемым id не существует")

if __name__ == '__main__':
    empty_library = Library()  # инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    
    library_with_books = Library(books=list_books)  # инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # проверяем следующий id для непустой библиотеки
    print(library_with_books.get_index_by_book_id(1)) # проверяем индекс книги с id = 1


