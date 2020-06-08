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


def breadth_first_way(tree):
    deque = collections.deque()
    root = list(tree)[0]
    deque.extend(root)
    search_list = []
    search_list.append(root)

    while deque:
        childs = tree[deque.popleft()]
        search_list.extend(childs)
        deque.extend(childs)
    return search_list


def breadth_first_search(tree, request):
    deque = collections.deque()
    root = list(tree)[0]
    deque.extend(root)

    while deque:
        childs = tree[deque.popleft()]
        if request in childs:
            return "Find"
        deque.extend(childs)

    return "Not find"


# print(breadth_first_way(tree))
print(breadth_first_search(tree, "Y"))
