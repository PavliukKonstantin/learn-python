# Для записи цифр римляне использовали буквы латинского алфафита:
# I, V, X, L, C, D, M. Например:
#
# 1 обозначалась с помощью буквы I
# 10 с помощью Х
# 7 с помощью VII
# Число 2020 в римской записи — это MMXX (2000 = MM, 20 = XX).
#
# Реализуйте функцию to_roman, которая переводит арабские числа в римские.
# Функция принимает на вход целое число из диапазона от 1 до 3000,
# а возвращает строку с римским представлением этого числа.
#
# Реализуйте функцию to_arabic, которая переводит число в римской записи
# в число, записанное арабскими цифрами.

# def to_arabic(number):  # noqa: WPS210
#     numbers = []
#     for char in number:
#         numbers.append(NUMERALS[char])
#     # Сдвиг чисел с повтором последнего
#     # Пример: [1,2,3,4] -> [2,3,4,4]
#     shifted_numbers = numbers[1:] + numbers[-1:]
#     result = 0
#     for previous, current in zip(numbers, shifted_numbers):
#         if previous >= current:
#             result += previous
#         else:
#             result -= previous
#     return result
arabic_numbers = {
    "I": 1, "IV": 4, "V": 5, "IX": 9,
    "X": 10, "XL": 40, "L": 50, "XC": 90,
    "C": 100, "CD": 400, "D": 500, "CM": 900, "M": 1000,
}.get


def to_arabic(number: str) -> int:
    if not number:
        return 0
    ch_num = number + "0"
    list_of_int = []
    i = 0
    while i < len(number):
        roman_number = arabic_numbers("{}{}".format(ch_num[i], ch_num[i + 1]))
        if roman_number is not None:
            list_of_int.append(roman_number)
            i += 2
        else:
            list_of_int.append(arabic_numbers(ch_num[i]))
            i += 1
    return sum(list_of_int)


print(to_arabic("MCDXCVIII"))


def test_to_arabic():
    assert to_arabic('') == 0
    assert to_arabic('I') == 1
    assert to_arabic('II') == 2
    assert to_arabic('IV') == 4
    assert to_arabic('V') == 5
    assert to_arabic('VI') == 6
    assert to_arabic('XXVII') == 27
    assert to_arabic('XLVIII') == 48
    assert to_arabic('LIX') == 59
    assert to_arabic('XCIII') == 93
    assert to_arabic('CXLI') == 141
    assert to_arabic('CLXIII') == 163
    assert to_arabic('CDII') == 402
    assert to_arabic('DLXXV') == 575
    assert to_arabic('CMXI') == 911
    assert to_arabic('MXXIV') == 1024
    assert to_arabic('MMXX') == 2020
    assert to_arabic('MMM') == 3000


test_to_arabic()
