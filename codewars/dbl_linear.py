# Consider a sequence u where u is defined as follows:

# The number u(0) = 1 is the first one in u.
# For each x in u, then y = 2 * x + 1 and z = 3 * x + 1 must be in u too.
# There are no other numbers in u.
# Ex: u = [1, 3, 4, 7, 9, 10, 13, 15, 19, 21, 22, 27, ...]

# 1 gives 3 and 4, then 3 gives 7 and 10, 4 gives 9 and 13,
# then 7 gives 15 and 22 and so on...

# Task:
# Given parameter n the function dbl_linear (or dblLinear...)
# returns the element u(n) of the ordered (with <) sequence u
# (so, there are no duplicates).

# from collections import deque

# def dbl_linear(n):
#     h = 1; cnt = 0; q2, q3 = deque([]), deque([])
#     while True:
#         if (cnt >= n):
#             return h
#         q2.append(2 * h + 1)
#         q3.append(3 * h + 1)
#         h = min(q2[0], q3[0])
#         if h == q2[0]: h = q2.popleft()
#         if h == q3[0]: h = q3.popleft()
#         cnt += 1
from datetime import datetime


def dbl_linear(n):
    lst = [1]
    y_i = 0
    z_i = 0
    y = 2 * lst[0] + 1
    z = 3 * lst[0] + 1
    while len(lst) < n + 1:
        if y < z:
            lst.append(y)
            y_i += 1
            y = 2 * lst[y_i] + 1
            continue
        if z != y:
            lst.append(z)
        z_i += 1
        z = 3 * lst[z_i] + 1
    return lst[n]


start = datetime.now()
print(dbl_linear((50)))
print("dbl_linear = {}".format(datetime.now() - start))

# testing(dbl_linear(10), 22)
# testing(dbl_linear(20), 57)
# testing(dbl_linear(30), 91)
# testing(dbl_linear(50), 175)
