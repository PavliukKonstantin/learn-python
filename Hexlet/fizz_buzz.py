# Реализуйте функцию fizz_buzz,
# которая возвращает строку с числами (через пробел)
# в диапазоне от begin до end включительно. При этом:
#
# Если число делится без остатка на 3, то вместо него выводится слово Fizz
# Если число делится без остатка на 5, то вместо него выводится слово Buzz
# Если число делится без остатка и на 3, и на 5,
# то вместо числа выводится слово FizzBuzz
# В остальных случаях в строку добавляется само число
# Функция принимает два параметра (begin и end),
# определяющих начало и конец диапазона (включительно).
# Если диапазон пуст (в случае, когда begin > end),
# то функция возвращает пустую строку.


def fizz_buzz(begin, end):
    string = ''
    for number in range(begin, end + 1):
        if not (number % 15):
            string += 'FizzBuzz '
        elif not (number % 3):
            string += 'Fizz '
        elif not (number % 5):
            string += 'Buzz '
        else:
            string += str(number) + ' '
    return string[:-1]


print(fizz_buzz(11, 20))


# print(list(map(lambda _: ("{}{}".format('Fizz' * (not _ % 5), 'Buzz' * (not _ % 3))) or _, range(1, 101))))


# def fizzbuzz(number):
#     return {
#         0: number,
#         number % 3: 'Fizz',
#         number % 5: 'Buzz',
#         number % 15: 'FizzBuzz',
#     }[0]
#
#
# for number in range(1, 101):
#     print(fizzbuzz(number))
