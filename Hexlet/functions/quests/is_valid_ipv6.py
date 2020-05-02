# Реализуйте функцию-предикат is_valid_ipv6, которая проверяет IPv6-адреса
# (адреса шестой версии интернет протокола) на корректность.
# Функция принимает на вход строку с адресом IPv6 и возвращает True,
# если адрес корректный, и False, если нет.
#
# Дополнительные условия:
#
# Работа функции не зависит от регистра символов.
# Ведущие нули в группах цифр необязательны.
# Самая длинная последовательность групп нулей, например, :0:0:0: может
# быть заменена на два двоеточия ::.
# Такую замену можно произвести только один раз.
# Одна группа нулей :0: не может быть заменена на ::.
# Примеры
# >>> from solution import is_valid_ipv6
# >>> is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d')
# True
# >>> is_valid_ipv6('::1')
# True
# >>> is_valid_ipv6('2607:G8B0:4010:801::1004')
# False
# >>> is_valid_ipv6('2.001::')
# False
# >>>


# def is_valid_group(group):
#     # Handle the error
#     # https://docs.python.org/3/tutorial/errors.html
#     try:
#         decimal = int(group, 16)
#     except ValueError:
#         return False
#     return decimal < 2 ** 16
#
#
# def is_valid_ipv6(ipv6):
#     if ipv6.count('::') > 1:
#         return False
#
#     groups = []
#
#     for group in filter(None, ipv6.split('::')):
#         groups.extend(group.split(':'))
#
#     is_full = '::' not in ipv6
#     length = len(groups) if is_full else len(groups) + 2
#     if length > 8 or (is_full and length < 8):
#         return False
#
#     return False not in map(is_valid_group, groups)

# def is_valid_ipv6(ipv6):
#     groups = []
#     if ipv6.find('::') != ipv6.rfind('::'):
#         return False
#     is_short = '::' in ipv6
#     for group in filter(None, ipv6.lower().split('::')):
#         groups.extend(group.split(':'))
#     lenght = len(groups) + 2 if is_short else len(groups)
#     if lenght > 8 or not is_short and lenght < 8:
#         return False
#     return all(
#         number and
#         not set(number) - set('01234567890abcdef') and
#         int(number, 16) < 2**16
#         for number in groups)
import re


def is_valid_ipv6(ip: str):
    regex = '|'.join((
        '(([0-9a-f]{1,4}:){7,7}[0-9a-f]{1,4})',
        '(([0-9a-f]{1,4}:){1,2}(:[0-9a-f]{1,4}){1,5})',
        '(:(:[0-9a-f]{1,4}){1,6})|',
        '([0-9a-f]{1,4}::[0-9a-f]{1,4})|',
        '(:{2}[0-9a-f]{1,4})|',
        '([0-9a-f]{1,4}::)|',
        '(::)',
    ))
    return (0, 1)[bool(re.fullmatch(regex, ip, flags=re.IGNORECASE))]


print("As first -> True")
print(is_valid_ipv6('::'))
print(is_valid_ipv6('::1'))
print(is_valid_ipv6('1::1'))


# print(is_valid_ipv6('::b36:3c:f0:7:937'))
# print(is_valid_ipv6('2a03:2880:2130:cf05:face:b00c:0:1'))
# print(is_valid_ipv6('000::B36:3C:00F0:7:937'))
# print(is_valid_ipv6('0B0:0F09:7f05:e2F3:0D:0:e0:7000'))
# print(is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d'))
# print(is_valid_ipv6('e:6c::647:50:0:7'))
# print(is_valid_ipv6('04:07A1:1404:0A0:A:080F:080:0'))
#
# print("Then -> False")
# print(is_valid_ipv6('2001'))
# print(is_valid_ipv6('2001:::'))
# print(is_valid_ipv6('2.001::'))
# print(is_valid_ipv6(':1::1'))
# print(is_valid_ipv6('1::1:'))
# print(is_valid_ipv6('2a02:0cb41:0:0:0:0:0:7'))
# print(is_valid_ipv6('2607:G8B0:4010:801::1004'))
# print(is_valid_ipv6('9f8:0:69S0:9:9:d9a:672:f90d'))
# print(is_valid_ipv6('1001:208:67:4f00:e3::2c6:0'))
# print(is_valid_ipv6('e1b6:1daf9:6:0:c50:8c4:90e:e'))
# print(is_valid_ipv6('C00D::a2195:2EA9:096'))
# print(is_valid_ipv6('d:0:4:a004:3b96:10b0:10:800:15'))
# print(is_valid_ipv6('5c03:0:a::b825:d690:4ce0:2831:acf0'))


def test_is_valid_ipv6():
    assert is_valid_ipv6('::')
    assert is_valid_ipv6('::1')
    assert is_valid_ipv6('1::1')
    assert is_valid_ipv6('::b36:3c:f0:7:937')
    assert is_valid_ipv6('2a03:2880:2130:cf05:face:b00c:0:1')
    assert is_valid_ipv6('000::B36:3C:00F0:7:937')
    assert is_valid_ipv6('0B0:0F09:7f05:e2F3:0D:0:e0:7000')
    assert is_valid_ipv6('10:d3:2d06:24:400c:5ee0:be:3d')
    assert is_valid_ipv6('e:6c::647:50:0:7')
    assert is_valid_ipv6('04:07A1:1404:0A0:A:080F:080:0')

    assert not is_valid_ipv6('2001')
    assert not is_valid_ipv6('2001:::')
    assert not is_valid_ipv6('2.001::')
    assert not is_valid_ipv6(':1::1')
    assert not is_valid_ipv6('1::1:')
    assert not is_valid_ipv6('2a02:0cb41:0:0:0:0:0:7')
    assert not is_valid_ipv6('2607:G8B0:4010:801::1004')
    assert not is_valid_ipv6('9f8:0:69S0:9:9:d9a:672:f90d')
    assert not is_valid_ipv6('1001:208:67:4f00:e3::2c6:0')
    assert not is_valid_ipv6('e1b6:1daf9:6:0:c50:8c4:90e:e')
    assert not is_valid_ipv6('C00D::a2195:2EA9:096')
    assert not is_valid_ipv6('d:0:4:a004:3b96:10b0:10:800:15')
    assert not is_valid_ipv6('5c03:0:a::b825:d690:4ce0:2831:acf0')


test_is_valid_ipv6()

# ::
# ::1
# 1::1
# ::b36:3c:f0:7:937
# 2a03:2880:2130:cf05:face:b00c:0:1
# 000::b36:3c:00f0:7:937
# 0B0:0f09:7f05:e2f3:0d:0:e0:7000
# 10:d3:2d06:24:400c:5ee0:be:3d
# e:6c::647:50:0:7
# 04:07a1:1404:0a0:a:080f:080:0
# 2001::
#
# 2001
# 2001:::
# 2.001::
# :1::1
# 1::1:
# 2a02:0cb41:0:0:0:0:0:7
# 2607:g8b0:4010:801::1004
# 9f8:0:69s0:9:9:d9a:672:f90d
# 1001:208:67:4f00:e3::2c6:0
# e1b6:1daf9:6:0:c50:8c4:90e:e
# c00d::a2195:2ea9:096
# d:0:4:a004:3b96:10b0:10:800:15
# 5c03:0:a::b825:d690:4ce0:2831:acf0
