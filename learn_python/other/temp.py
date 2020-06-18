from itertools import zip_longest
a = ["a", "b", "c", "d", "e"]
b = [1, 2, 3, 4]


def kv_dict(key, value):
    return dict(zip_longest(key, value[:len(key)]))


print(kv_dict(a, b))
