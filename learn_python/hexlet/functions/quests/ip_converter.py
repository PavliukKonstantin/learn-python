# Реализуйте и экспортируйте функции ip2int и int2ip,
# которые преобразовывают представление IP-адреса
# из десятичного формата с точками в 32-битное число
# в десятичной форме и обратно.
#
# Функция ip2int на вход строку и должна возвращать число.
# А функция int2ip наоборот: принимает на вход число, а возвращает строку.
#
# Примеры
# >>> ip2int('128.32.10.1')
# 2149583361
# >>> ip2int('0.0.0.0')
# 0
# >>> ip2int('255.255.255.255')
# 4294967295
# >>>
# >>> int2ip(2149583361)
# '128.32.10.1'
# >>> int2ip(0)
# '0.0.0.0'
# >>> int2ip(4294967295)
# '255.255.255.255'


# def ip2int(ip):
#     return int.from_bytes(map(int, ip.split('.')), byteorder='big')
#
#
# def int2ip(number):
#     return '.'.join([str(i) for i in number.to_bytes(4, byteorder='big')])


def ip2int(ip: str) -> int:
    octets = (int(i) for i in ip.split("."))
    return int("{:08b}{:08b}{:08b}{:08b}".format(*octets), 2)


def int2ip(ip: int) -> str:
    octets = map(''.join, zip(*(iter("{:032b}".format(ip)),) * 8))
    return "{0}.{1}.{2}.{3}".format(*(int(i, 2) for i in octets))


# print(int2ip(1))

# ip = 0
# answer = '128.32.10.1'
#
# # b = "{:32b}".format(ip)
#
# c = [int(i, 2) for i in map(''.join, zip(*[iter("{:032b}".format(ip))]*8))]
#
# b = "{0}.{1}.{2}.{3}".format(*c)
#
#
# print(c)
# print(b)


ZEROES = '0.0.0.0'  # noqa: S104


def test_ip2int():
    assert ip2int(ZEROES) == 0
    assert ip2int('128.32.10.1') == 2149583361


def test_int2ip():
    assert int2ip(0) == ZEROES
    assert int2ip(2149583361) == '128.32.10.1'


def test_round_robin():
    assert int2ip(ip2int('192.168.1.32')) == '192.168.1.32'
    assert ip2int(int2ip(2149583361)) == 2149583361


test_int2ip()
test_ip2int()
test_round_robin()
