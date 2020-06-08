# digital_root(16)
# => 1 + 6
# => 7
#
# digital_root(942)
# => 9 + 4 + 2
# => 15 ...
# => 1 + 5
# => 6
#
# digital_root(132189)
# => 1 + 3 + 2 + 1 + 8 + 9
# => 24 ...
# => 2 + 4
# => 6

# def digital_root(n):
#     return n % 9 or n and 9


# def digital_root(n):
#     n = sum([int(i) for i in str(n)])
#     if n > 9:
#         return digital_root(n)
#     return n

def digital_root(n):
    return n if n < 10 else digital_root(sum(map(int, str(n))))


# n = 132189
#
# b = sum([int(i) for i in str(n)])
# print(b)
print(digital_root(132189))
