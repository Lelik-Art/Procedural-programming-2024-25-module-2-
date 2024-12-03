import doctest


class Applicants:
    def __init__(self, app_id: int, points: int):
        """
        Создание и подготовка к работе объекта "Абитуриенты"

        :param app_id: Индивидуальный номер абитуриента
        :param points: Количество баллов ЕГЭ абитуриента

        :raise TypeError: Если тип ID не является int, возвращается ошибка
        :raise ValueError: Если ID состоит не из 5 цифр, возвращается ошибка
        :raise ValueError: Если количество баллов отрицательное или превышает максимальное значение, возвращается ошибка

        Примеры:
        >>> applicant = Applicants(12345, 179) 
        """
        if not isinstance(app_id, int):
            raise TypeError("ID должен быть типа int")
        if len(str(app_id)) != 5:
            raise ValueError("ID должен состоять из 5 символов")

        self.app_id = app_id

        if not isinstance(points, int) or points < 0 or points >= 310:
            raise ValueError(
                "Значение баллов должно лежать в промежутке от 0 до 310")
        self.points = points

    def add_points(self, additional_points: int) -> int:
        """
        Функция которая добавляет доп баллы к основным

        :param additional_points: Количество доп баллов абитуриента

        :raise ValueError: Если количество доп баллов больше разрешенного (10) или меньше возможного (0), то возвращается ошибка

        :return: Общее количество баллов с учетом дополнительных

        Примеры:
        >>> applicant = Applicants(12345, 179)
        >>> result = applicant.add_points(10)
        """
        if additional_points > 10 or additional_points < 0:
            raise ValueError("Введено некорректное количество баллов")
        else:
            self.points = self.points + additional_points
        return self.points

    def enroll(self, min_points: int = 180) -> str:
        """
        Функция, которая зачисляет студентов

        :param min_points: Минимальное количество баллов для поступления

        :return: Результат поступления

        Примеры:
        >>> applicant = Applicants(12345, 179)
        >>> result = applicant.enroll()
        """
        if self.points >= min_points:
            result = "Абитуриент зачислен"
        else:
            result = "Абитуриент не зачислен"
        return result


if __name__ == "__main__":
    doctest.testmod()


class Sweets_jar:
    def __init__(self, ch_cand: int, caramels: int, max_cand: int = 20, started_caramels: int = 3):
        """
        Создание и подготовка к работе объекта "Банка с конфетами"

        :param ch_cand: Количество добавленных в банку шоколадных конфет
        :param caramels: Количество добавленных в банку карамелек
        :param max_cand: Максимально допустимое количество конфет в банке
        :param started_caramels: Изначальное количество карамелек в банке

        :raise TypeError: Если тип количества конфет не является int, возвращается ошибка
        :raise ValueError: Если Количество конфет отрицательное или больше допустимого значния, возвращается ошибка

        Примеры:
        >>> jar = Sweets_jar(2, 4)  # инициализация экземпляра класса
        """
        if not isinstance(ch_cand, int) or not isinstance(caramels, int):
            raise TypeError("Тип количества конфет должен быть int")
        if ch_cand < 0 or caramels < 0:
            raise ValueError("Количество конфет не может быть отрицательным")
        if ch_cand + caramels > 20:
            raise ValueError("Превышено допустимое количество конфет")

        self.ch_cand = ch_cand
        self.caramels = caramels + started_caramels

        self.max_cand = max_cand
        self.started_caramels = started_caramels

    def take_candy(self, take_ch: int, take_caramels: int, min_caramels: int = 2) -> str:
        """
        Функция, которая изымает конфеты из банки

        :param take_ch: Количество изымыемых из банки шоколадных конфет
        :param take_caramels: Количество изымыемых из банки карамелек
        :param min_caramels: Минимальный допустимый остаток карамелек (мама ругается, если в банке не осталось конфет...)

        :raise TypeError: Если количество взятых конфет не является типом int, возвращается ошибка
        :raise ValueError: Если попытались взять отрицательное количество конфет, большее, чем есть в банке или в банке 
        остается меньше допустимого остатка, возвращается ошибка

        :return: Остаток шоколадных и карамельных конфет

        Примеры:
        >>> jar = Sweets_jar(2, 4)
        >>> result = jar.take_candy(2, 1)
        """
        if not isinstance(take_ch, int) or not isinstance(take_caramels, int):
            raise TypeError("Количество взятых конфет должно иметь тип int")
        if take_ch < 0 or take_caramels < 0:
            raise ValueError("Нельзя взять отрицательное число конфет")
        if take_caramels + self.caramels < min_caramels:
            raise ValueError(
                "Нельзя оставить в банке меньше минимального допустимого остатка")
        if take_ch > self.ch_cand or take_caramels > self.caramels:
            raise ValueError(
                "Нельзя взять больше конфет, чем находится в банке")

        self.ch_cand -= take_ch
        self.caramels -= take_ch

        result = f"В банке осталось {self.ch_cand} шоколадных конфет и {self.caramels} карамелек"

        return (result)

    def put_candy(self, put_ch: int, put_caramels: int) -> str:
        """
        Функция, которая добавляет конфеты в банку

        :param put_ch: Количество добавляемых в банку шоколадных конфет
        :param put_caramels: Количество добавляемых в банку карамелек

        :raise TypeError: Если количество добавленных конфет не является типом int, возвращается ошибка
        :raise ValueError: Если попытались добавить отрицательное количество конфет или больше, чем может вместить банка, возвращается ошибка

        :return: Остаток шоколадных и карамельных конфет

        Примеры:
        >>> jar = Sweets_jar(2, 4)
        >>> result = jar.put_candy(2, 1)
        """
        if not isinstance(put_ch, int) or not isinstance(put_caramels, int):
            raise TypeError(
                "Количество добавленных конфет должно иметь тип int")
        if put_ch < 0 or put_caramels < 0:
            raise ValueError("Нельзя положить отрицательное число конфет")
        if self.ch_cand + self.caramels + put_ch + put_caramels > self.max_cand:
            raise ValueError(
                "Нельзя положить в банку больше конфет, чем она вмещает")

        self.ch_cand += put_ch
        self.caramels += put_caramels

        result = f"В банке осталось {self.ch_cand} шоколадных конфет и {self.caramels} карамелек"

        return (result)


if __name__ == "__main__":
    doctest.testmod()


class Coffee_cup():
    def __init__(self, sort: str, base_price: int = 90):
        """
        Создание и подготовка к работе объекта "Чашка кофе"

        :param sort: Сорт кофе (арабика или робуста)
        :param base_price: Минимальная цена чашки кофе

        :raise ValueError: Если указан неверный сорт кофе (не arabic или robusta), возвращается ошибка

        Примеры:
        >>> cup = Coffee_cup("robusta")  # инициализация экземпляра класса
        """

        if sort != "arabic" and sort != "robusta":
            raise ValueError(
                "Нужно выбрать один из двух сортов кофе: arabic или robusta")

        self.sort = sort

        if self.sort == "robusta":
            self.price = base_price
        else:
            self.price = base_price + 10

        self.base_price = base_price

    def add_milk(self, value: bool, price_premium: int = 50) -> int:
        """
        Функция, которая добавляет молоко в кофе и повышает его стоимость

        :param value: Наличие или отсутствие зароса на молоко
        :param price_premium: Повышение цены при добавлении молока

        :raise TypeError: Если значение наличия или отсутствия молока имеет не тип bool, возвращается ошибка

        :return: Стоимость кофе после добавления молока

        Примеры:
        >>> cup = Coffee_cup("robusta")
        >>> result = cup.add_milk(True)
        """
        if type(value) != bool:
            raise TypeError(
                "Значение наличия или отсутствия молока должно иметь тип bool")

        if value == True:
            self.price += price_premium

        return self.price

    def add_syrop(self, value: bool, price_premium: int = 20) -> int:
        """
        Функция, которая добавляет сироп в кофе и повышает его стоимость

        :param value: Наличие или отсутствие зароса на сироп
        :param price_premium: Повышение цены при добавлении сиропа

        :raise TypeError: Если значение наличия или отсутствия сиропа имеет не тип bool, возвращается ошибка

        :return: Стоимость кофе после добавления сиропа

        Примеры:
        >>> cup = Coffee_cup("robusta")
        >>> result = cup.add_syrop(True)
        """
        if type(value) != bool:
            raise TypeError(
                "Значение наличия или отсутствия сиропа должно иметь тип bool")

        if value == True:
            self.price += price_premium

        return self.price


if __name__ == "__main__":
    doctest.testmod()
