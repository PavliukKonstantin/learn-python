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
# Реализуйте функцию to_arabic, которая переводит число в римской
# записи в число, записанное арабскими цифрами.

# def descending(pair):
#     return -pair[1]
#
#
# def to_roman(number):
#     result = ''
#     for roman, arabic in sorted(NUMERALS.items(), key=descending):
#         repetitions_count = number // arabic
#         number -= arabic * repetitions_count
#         result += roman * repetitions_count
#     return result


roman_numbers = {
    1: "I", 4: "IV", 5: "V", 9: "IX",
    10: "X", 40: "XL", 50: "L", 90: "XC",
    100: "C", 400: "CD", 500: "D", 900: "CM", 1000: "M",
}.get


def to_roman(number: int) -> str:
    if not number:
        return ''
    number_how_list = []
    for __ in range(len(str(number))):
        number_how_list.append(number % 10)
        number //= 10
    list_of_int = []
    i = 0
    for num in number_how_list:
        order = pow(10, i)
        num *= order
        while num != 0:
            if roman_numbers(num) is None:
                list_of_int.append(order)
                num -= order
            else:
                list_of_int.append(num)
                num -= num
        i += 1
    return ''.join(reversed([roman_numbers(__) for __ in list_of_int]))


print(to_roman(1498))


def test_to_roman():
    assert to_roman(0) == ''
    assert to_roman(1) == 'I'
    assert to_roman(2) == 'II'
    assert to_roman(4) == 'IV'
    assert to_roman(5) == 'V'
    assert to_roman(6) == 'VI'
    assert to_roman(27) == 'XXVII'
    assert to_roman(48) == 'XLVIII'
    assert to_roman(59) == 'LIX'
    assert to_roman(93) == 'XCIII'
    assert to_roman(141) == 'CXLI'
    assert to_roman(163) == 'CLXIII'
    assert to_roman(402) == 'CDII'
    assert to_roman(575) == 'DLXXV'
    assert to_roman(911) == 'CMXI'
    assert to_roman(1024) == 'MXXIV'
    assert to_roman(2020) == 'MMXX'
    assert to_roman(3000) == 'MMM'


test_to_roman()
