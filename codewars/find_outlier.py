# You are given an array (which will have a length of at least 3, but
# could be very large) containing integers. The array is either entirely
# comprised of odd integers or entirely comprised of even integers except for
# a single integer N. Write a method that takes the array as an argument
# and returns this "outlier" N.
#
#
# Examples
# [2, 4, 0, 100, 4, 11, 2602, 36]
# Should return: 11 (the only odd number)
#
# [160, 3, 1719, 19, 11, 13, -21]
# Should return: 160 (the only even number)
from itertools import dropwhile
from datetime import datetime


start_time1 = datetime.now()
integers = [x for x in range(100000000) if x & 1] + [160]
print("Create list = {}".format(datetime.now() - start_time1))


# def find_outlier(integers):
#     return next(dropwhile(lambda x: (not x & 1, x & 1)[sum(i & 1 for i in integers[:3]) > 1], set(integers)))


def find_outlier(integers):
    return next(x for x in set(integers) if (x & 1, not x & 1)[sum(i & 1 for i in integers[:3]) > 1])


# integers = [160, 3, 1719, 19, 11, 13, -21]


print(integers[:3])

start_time2 = datetime.now()
print(next(dropwhile(lambda x: (not x & 1, x & 1)[sum(i & 1 for i in integers[:3]) > 1], set(integers))))
print("Time Second = {}".format(datetime.now() - start_time2))

start_time3 = datetime.now()
print(next(x for x in set(integers) if (x & 1, not x & 1)[sum(i & 1 for i in integers[:3]) > 1]))
print("Time First = {}".format(datetime.now() - start_time3))




# test.assert_equals(find_outlier([2, 4, 6, 8, 10, 3]), 3)
# test.assert_equals(find_outlier([2, 4, 0, 100, 4, 11, 2602, 36]), 11)
# test.assert_equals(find_outlier([160, 3, 1719, 19, 11, 13, -21]), 160)
