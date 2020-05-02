# Реализуйте и функцию is_power_of_three, которая определяет, является ли переданное число натуральной степенью тройки.
# Например, число 27 — это третья степень: 3 ** 3, а 81 — это четвёртая: 3 ** 4.

from datetime import datetime
from math import log

a = 3 ** 10000000

start_time = datetime.now()


def is_power_of_three(number):
    return (log(number, 3)).is_integer()


# def is_power_of_three(number):
#     if number < 1:
#         return False
#     while number != 3 and number > 1:
#         if (number ** 0.5).is_integer():
#             number **= 0.5
#         else:
#             return False
#     return True

# def is_power_of_three(number):
#     counter = 1
#     while counter < number:
#         counter *= 3
#     return counter == number


print(is_power_of_three(a))

print(datetime.now() - start_time)
