# Реализуйте абстракцию для работы с рациональными числами
# включающую в себя следующие функции:
#
# Конструктор make_rational — принимает на вход числитель и знаменатель,
# возвращает дробь.
# Селектор get_numer — возвращает числитель
# Селектор get_denom — возвращает знаменатель
# Сложение add — складывает переданные дроби
# Вычитание sub — находит разность между двумя дробями
# Не забудьте реализовать нормализацию дробей удобным для вас способом.
#
# >>> rat1 = make_rational(3, 9)
# >>> get_numer(rat1)
# 1
# >>> get_denom(rat1)
# 3
#
# >>> rat2 = make_rational(10, 3)
#
# >>> rat3 = add(rat1, rat2)
# >>> rat_to_string(rat3)
# 11/3
#
# >>> rat4 = sub(rat1, rat2)
# >>> rat_to_string(rat4)
# -3/1
# Подсказки
# Функция gcd из модуля math находит наибольший общий делитель двух чисел
# Функция rat_to_string возвращает строковое представление числа
# (используется для отладки)
# Функция int преобразует значение к целому числу
import math


def make_rational(numer, denom):
    gcd = math.gcd(numer, denom)
    return {"numer": numer // gcd, "denom": denom // gcd}


def get_numer(rat):
    return rat["numer"]


def get_denom(rat):
    return rat["denom"]


def add(rat1, rat2):
    numer1 = get_numer(rat1) * get_denom(rat2)
    numer2 = get_numer(rat2) * get_denom(rat1)
    numer = numer1 + numer2
    denom = get_denom(rat1) * get_denom(rat2)
    return make_rational(numer, denom)


def sub(rat1, rat2):
    numer1 = get_numer(rat1) * get_denom(rat2)
    numer2 = get_numer(rat2) * get_denom(rat1)
    numer = numer1 - numer2
    denom = get_denom(rat1) * get_denom(rat2)
    return make_rational(numer, denom)


def rat_to_string(rat):
    return "{}/{}".format(get_numer(rat), get_denom(rat))


rat_1 = make_rational(3, 9)
rat_2 = make_rational(10, 3)
print(get_numer(rat_1))
print(get_denom(rat_1))

print(rat_1)
print(rat_2)

rat_3 = add(rat_1, rat_2)
print(rat_3)
rat_4 = sub(rat_1, rat_2)
print(rat_4)


def test_rational():
    rat1 = make_rational(3, 9)
    assert get_numer(rat1) == 1
    assert get_denom(rat1) == 3

    rat2 = make_rational(10, 3)
    assert add(rat1, rat2) == make_rational(11, 3)
    assert sub(rat1, rat2) == make_rational(-3, 1)

    rat3 = make_rational(-4, 16)
    assert get_numer(rat3) == -1
    assert get_denom(rat3) == 4

    rat4 = make_rational(12, 5)
    assert add(rat3, rat4) == make_rational(43, 20)
    assert sub(rat3, rat4) == make_rational(-53, 20)

    assert rat_to_string(rat1) == "1/3"
    assert rat_to_string(rat3) == "-1/4"


test_rational()
