# В этом упражнении вам нужно будет реализовать две функции высшего порядка,
# возвращающие замыкания: partial_apply и flip.
#
# partial_apply
# partial_apply принимает функцию от двух аргументов и первый аргумент,
# а возвращает замыкание — функцию, которая примет второй аргумент и наконец
# применит замкнутую функцию к обоим аргументам (и вернёт результат).
#
# Пример использования:
#
# >>> def greet(name, surname):
# ...     return 'Hello, {name} {surname}!'.format(name=name, surname=surname)
# ...
# >>> f = partial_apply(greet, 'Dorian')
# >>> f('Grey')
# 'Hello, Dorian Grey!'
# >>>
# flip
# Функция flip принимает в качестве единственного аргумента функцию от двух
# аргументов. Возвращаемое замыкание должно также принять два аргумента,
# а затем применить к ним замкнутую функцию, но аргументы подставить в обратном
# порядке.
# Таким образом flip как бы "переворачивает" ("flips") исходную функцию.
#
# Пример использования:
#
# >>> def greet(name, surname):
# ...     return 'Hello, {name} {surname}!'.format(name=name, surname=surname)
# ...
# >>> f = flip(greet)
# >>> f('Christian', 'Teodor')
# 'Hello, Teodor Christian!'


from operator import add, mul


def greet(name, surname):
    return 'Hello, {name} {surname}!'.format(name=name, surname=surname)


def partial_apply(function, first_arg):
    def inner(second_arg):
        return function(first_arg, second_arg)

    return inner


f = partial_apply(greet, 'Dorian')('Grey')
print(f)


def flip(function):
    def inner(first_arg, second_arg):
        return function(second_arg, first_arg)

    return inner


g = flip(greet)('Christian', 'Teodor')
print(g)


def test_partial_apply():
    assert list(
        map(partial_apply(add, 10), [1, 2, 3]),  # noqa: WPS221
    ) == [11, 12, 13]

    assert list(
        map(partial_apply(mul, '*'), [2, 3, 4]),  # noqa: WPS221
    ) == [
               '**',
               '***',
               '****',
           ]


def test_flip():
    assert flip(mul)(3, '*') == '***'


def test_both():
    assert list(
        map(partial_apply(flip(mul), 5), "!?&"),
    ) == [
               '!!!!!',
               '?????',
               '&&&&&',
           ]


test_both()
test_flip()
test_partial_apply()
