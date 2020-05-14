# Реализуйте функцию-предикат scrabble, которая принимает на вход два параметра:
# набор символов (строку) и слово,
# и проверяет, можно ли из переданного набора составить это слово.
# В результате вызова функция возвращает True или False.
#
# При проверке учитывается количество символов, которые нужны для составления
# слова, и не учитывается их регистр.
#
# Для решения используйте встроенный инструмент — Counter.
from collections import Counter


# def scrabble(string, word):
#     letters = Counter(string.lower())
#     for letter, count in Counter(word.lower()).items():
#         if letters[letter] < count:
#             return False
#     return True
#
#     # Можно было сделать ещё короче, если учесть то,
#     # как работает вычитание для пары Counter!
#     # Хватило бы: return not (Counter(word.lower()) - Counter(string.lower()))


def scrabble(string: str, word: str):
    count_str = Counter(string.lower())
    count_word = Counter(word.lower())
    for i in count_word:
        if count_str.get(i) is None or count_str.get(i) < count_word.get(i):
            return False
    return True


_word = Counter('aabc'.lower())
_string = Counter('abcc'.lower())

print(_word, _string)
print(_word - _string)


def test_scrabble():
    assert scrabble('begsdhhtsexoult', 'hexlet') is True
    assert scrabble('rkqodlw', 'world') is True
    assert scrabble('begsdhhtsexoult', 'hexlet') is True
    assert scrabble('katas', 'steak') is False
    assert scrabble('scriptjava', 'javascript') is True
    assert scrabble('scriptingjava', 'javascript') is True
    assert scrabble('scriptjavest', 'javascript') is False
    assert scrabble('', 'hexlet') is False
    assert scrabble('scriptingjava', 'JavaScript') is True


test_scrabble()
