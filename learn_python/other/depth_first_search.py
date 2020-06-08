import collections

tree = {
    "A": ("B", "C", "O"),
    "B": ("D", "E"),
    "C": ("K", "L"),
    "D": ("G", "H"),
    "E": ("F"),
    "F": (),
    "G": (),
    "H": ("I", "J"),
    "I": (),
    "J": (),
    "K": ("M", "N"),
    "L": (),
    "M": (),
    "N": (),
    "O": ("P", "Q"),
    "P": (),
    "Q": ("R", "S"),
    "R": (),
    "S": ("T"),
    "T": ("U"),
    "U": (),
}


def depth_first_nlr(tree):
    deque = collections.deque()
    root = list(tree)[0]
    deque.extend(root)
    search_list = []

    while deque:
        parent = deque.popleft()
        search_list.extend(parent)
        childs = tree[parent]
        deque.extendleft(reversed(childs))
        # print(deque)
    return search_list


# def depth_first_lnr(tree):
#     descent_deque = collections.deque()
#     rise_deque = collections.deque()
#     root = list(tree)[0]
#     descent_deque.extend(root)
#     search_list = []

#     while descent_deque:
#         parent = descent_deque.popleft()
#         childs = tree[parent]
#         if childs:
#             rise_deque.appendleft(parent)
#             descent_deque.extendleft(reversed(childs))
#         else:
#             search_list.append(parent)
#             search_list.append(rise_deque.popleft())
#         print("Descent: {}".format(descent_deque))
#         print("Rise: {}".format(rise_deque))

#     return search_list


print(depth_first_nlr(tree))
