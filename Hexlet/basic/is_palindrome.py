# Реализуйте функцию is_palindrome, которая принимает на вход слово,
# определяет является ли оно палиндромом и возвращает логическое значение.


# def is_palindrome(string):
#     i = 0
#     out = True
#     while i < len(string) - 1:
#         if string[i] != string[-(i+1)]:
#             out = False
#             break
#         i += 1
#     return out

def is_palindrome(string):
    return string == string[::-1]


print(is_palindrome('radar1'))
