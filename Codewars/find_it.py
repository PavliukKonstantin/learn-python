# Given an array, find the integer that appears an odd number of times.
#
# There will always be only one integer that appears an odd number of times.
from collections import Counter


# def find_it(seq):
#     for k, v in Counter(seq).items():
#         if v % 2:
#             return k

def find_it(seq):
    for i in set(seq):
        if seq.count(i) % 2 != 0:
            return i


a = [20, 1, -1, 2, -2, 3, 3, 5, 5, 1, 2, 4, 20, 4, -1, -2, 5]

b = Counter(a)
print(find_it(a))

# test.assert_equals(find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]), 5)
# test.assert_equals(find_it([1,1,2,-2,5,2,4,4,-1,-2,5]), -1);
# test.assert_equals(find_it([20,1,1,2,2,3,3,5,5,4,20,4,5]), 5);
# test.assert_equals(find_it([10]), 10);
# test.assert_equals(find_it([1,1,1,1,1,1,10,1,1,1,1]), 10);
# test.assert_equals(find_it([5,4,3,2,1,5,4,3,2,10,10]), 1);
