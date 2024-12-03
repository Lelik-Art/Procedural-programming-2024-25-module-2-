from task_1 import Applicants, Sweets_jar, Coffee_cup


if __name__ == "__main__":

    person = Applicants(12345, 234)
    jar = Sweets_jar(2, 4)
    сup = Coffee_cup("robusta")

    try:
        person.add_points(15)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        jar.take_candy(2, -10)
    except TypeError:
        print('Ошибка: неправильные данные')

    try:
        cup.add_milk(10)
    except TypeError:
        print('Ошибка: неправильные данные')
