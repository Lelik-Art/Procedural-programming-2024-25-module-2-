class Social_networks:
    def __init__(self, name: str, age: int):
        """
        Создание и подготовка к работе объекта "Социальные сети"

        :param name: Имя пользователя
        :param age: Возраст пользователя

        :raise TypeError: Если тип имени не является str, возвращается ошибка (проверка реализуется через функцию set_name)
        :raise TypeError: Если тип возраста не является int, возвращается ошибка (проверка реализуется через функцию set_age)
        :raise ValueError: Если возраст отрицательный или превышает максимальное значение, возвращается ошибка (проверка реализуется через функцию set_age)

        Примеры:
        >>> person = Social_networks("Арсений", 16) 
        """

        self.name = None
        self.set_name(name)

        self.age = None
        self.set_age(age)

    def find_person(self, p_age: int, gender: str) -> str:
        """
        Функция, которая принимает данные для поиска человека

        :param p_age: Возраст искомого человека
        :param gender: Пол искомого человека

        :raise ValueError: Если возраст отрицательный или превышает максимальное значение, возвращается ошибка (проверка реализуется через функцию set_p_age)
        :raise ValueError: Если гендер принимает значение отличное от "мужской" или "женский", возвращается ошибка (проверка реализуется через функцию set_gender)

        :return: Пол и возраст искомого человека

        Примеры:
        >>> person = Social_networks("Арсений", 16)
        >>> result = person.find_person(16, "женский")
        """
    
        self.p_age = None
        self.set_p_age(p_age)

        self.gender = None
        self.set_gender(gender)

        return f"Ваш запрос для поиска: возраст - {self.p_age}, пол - {self.gender}"
        
    def status(self, text: str) -> str: 
        """
        Функция устанавливает статус пользователя

        :param text: Устанавливаемый статус

        :return: Установленный статус

        Примеры:
        >>> person = Social_networks("Арсений", 16)
        >>> result = person.status("Все сложно")
        """
        return f"Статус пользователя: {text}"

    def set_name(self, new_name: str):
        """
        Функция осуществляет проверку переменной name

        :param new_name: Проверяемое имя
        """
        if not isinstance(new_name, str):
            raise TypeError("Имя должно иметь тип данных str")
        else:
            self.name = new_name

    def set_age(self, new_age: int):
        """
        Функция осуществляет проверку переменной age

        :param new_age: Проверяемый возраст
        """
        if not isinstance(new_age, int):
            raise TypeError("Возраст должен иметь тип int")
        elif new_age < 0 or new_age > 120:
            raise ValueError("Возраст не должен быть отрицательным или быть выше 120 лет")
        else:
            self.age = new_age

    def set_p_age(self, new_p_age: int):
        """
        Функция осуществляет проверку переменной p_age

        :param new_p_age: Проверяемый возраст искомого человека
        """
        if not isinstance(new_p_age, int):
            raise TypeError("Возраст должен иметь тип int")
        elif new_p_age < 0 or new_p_age > 120:
            raise ValueError("Возраст не должен быть отрицательным или быть выше 120 лет")
        else:
            self.p_age = new_p_age

    def set_gender(self, new_gender: str):
        """
        Функция осуществялет проверку переменной gender

        :param new_gender: Проверяемый гендер искомого человека
        """
        if new_gender == "женский" or new_gender == "мужской":
            self.gender = new_gender
        else:
            raise ValueError("Гендер может принимать значение женский или мужской")

    def __str__(self) -> str:
        """
        Получение строкового представления объекта для пользователя

        :return: Строковое представление объекта для пользователя
        """
        return f"Имя {self.name!r}. Возраст {self.age}"

    def __repr__(self) -> str:
        """
        Получение строкового представления объекта для разработчика

        :return: Строковое представление объекта для разработчика
        """
        return f"name={self.name!r}, age={self.age}"

class LinkedIn(Social_networks):
    """
    Класс социальной сети LinkedIn, наследующий класс Social_networks

    Функции __init__, __str__, __repr__ полностью наследуются
    """
    def status(self, status: str) -> str:
        """
        Функция, устанавливающая статус пользователя, перегружается с наследуемого класса.
        Причина перегрузки: разное функциональное значение понятия статус в рамках социальной сети

        :param status: Статус пользователя

        :raise ValueError: Если статус принимает значение отличное от "работник" или "работодатель", то возвращается ошибка (проверка реализуется через функцию set_status)

        :return: Статус пользователя
        """
        self.status = None
        self.set_status(status)

        return f"Статус пользователя: {self.status}"

    def set_status(self, new_status: str):
        """
        Функция осуществялет проверку переменной status

        :param new_status: Проверяемый статус пользователя
        """
        if new_status == "работник" or new_status == "работодатель":
            self.status = new_status
        else:
            raise ValueError("Статус может принимать значение работодатель или работник")

    

