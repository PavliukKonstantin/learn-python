# В этом испытании вы будете работать с "тройками" — кортежами из трёх элементов.
# Вам предстоит реализовать две функции, которые "вращают" тройку влево и вправо.

input1 = ('A', 'B', 'C')


def rotate_left(triple):
    (a, b, c) = triple
    triple = (b, c, a)
    return triple


def rotate_right(triple):
    (a, b, c) = triple
    triple = (c, a, b)
    return triple


print(rotate_left(input1))
print(rotate_right(input1))
