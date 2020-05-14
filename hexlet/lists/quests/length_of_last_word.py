# Реализуйте функцию length_of_last_word, которая возвращает длину последнего слова переданной на вход строки.
# Словом считается любая последовательность, не содержащая пробелов.


def length_of_last_word(foo):
    if foo.isspace() or not foo:
        return 0
    return len(foo.split()[-1])


a = 'hello, world!     '
b = '  '
c = ''

print(length_of_last_word(c))
