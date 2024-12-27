"""
1)Для классов Book, PaperBook, AudioBook примените наследование.
2)Исходя из кода, подумайте, когда методы __str__ и __repr__ могут быть унаследованы, а когда перегружены в дочерних классах. Исправьте это.
3)Атрибуты name и author изменяться не могут, поэтому напишите для них свойства, которые не позволят изменять эти атрибуты.
4)Так как на pages и duration накладываются ограничения по типу и допустимым значениям, напишите для них свойства
с проверками при присвоении им значений (должны выбрасываться исключения TypeError и ValueError соответственно).
"""


class Book:
    def __init__(self, name: str, author: str):
        self.name = name
        self.author = author

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value: str):
        self._author = value

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super(PaperBook, self).__init__(name, author)
        self.pages = None
        self.set_pages(pages)

    def set_pages(self, new_pages: int):
        if not isinstance(new_pages, int):
            raise TypeError("Количество страниц должно иметь тип int")
        elif new_pages < 0:
            raise ValueError("Количество страниц не должно быть отрицательным")
        else:
            self.pages = new_pages

    def __str__(self):
        return f"{super().__str__()}, количество страниц: {self.pages}"

    def __repr__(self):
        return f"{super().__repr__()}, pages = {self.pages}"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super(AudioBook, self).__init__(name, author)
        self.duration = duration

    def set_duration(self, pages:  int):
        if not isinstance(duration, int) and not isinstance(duration, float):
            raise TypeError("Продолжительность записи должна иметь тип int")
        if duration < 0:
            raise ValueError(
                "Продолжительность записи не должна быть отрицательным")

    def __str__(self):
        return f"{super().__str__()}, продолжительность записи: {self.duration}"

    def __repr__(self):
        return f"{super().__repr__()}, duration = {self.duration}"
