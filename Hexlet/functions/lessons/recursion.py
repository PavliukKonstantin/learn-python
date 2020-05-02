# В упражнении вам нужно будет реализовать две взаимно рекурсивные функции
# (то есть использующие косвенную рекурсию):
#
# is_odd должна возвращать True, если число нечётное,
# is_even должна возвращать True, если число чётное.
# Для простоты считаем, что аргументы всегда будут неотрицательными.
#
# Вы, конечно, можете реализовать функции независимыми.
# Но задание призывает попробовать именно косвенную рекурсию!
#
# Примеры
# >>> is_odd(42)
# False
# >>> is_odd(99)
# True
# >>> is_even(42)
# True
# >>> is_even(99)
# False

# def is_odd(number):
#     return False if number == 0 else is_even(number - 1)
#
#
# def is_even(number):
#     return True if number == 0 else is_odd(number - 1)


def is_odd(num):
    return bool(num % 2)


def is_even(num):
    return not bool(num % 2)


print(is_odd(42))
print(is_odd(99))
print(is_even(42))
print(is_even(99))


def test_is_odd():
    assert not is_odd(42)
    assert is_odd(99)


def test_is_even():
    assert not is_even(99)
    assert is_even(42)

# test_is_even()
# test_is_odd()
