# Вес Хэмминга это количество единиц в двоичном представлении числа.
# Реализуйте функцию hamming_weight, которая считает вес Хэмминга.


def hamming_weight(number):
    return format(number, 'b').count('1')


print(hamming_weight(12345))
