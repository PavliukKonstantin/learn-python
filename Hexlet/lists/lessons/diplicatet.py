# Вам необходимо реализовать функцию duplicate, которая должна принимать в качестве аргумента список и
# удваивать этот список "по месту" (вам нужно будет изменять исходный объект списка.
# Помним: список передаётся по ссылке!).
# Удваивание здесь означает, что после применения к нему функции список должен иметь копию всех элементов,
# добавленную в конец (см. пример ниже).


def duplicate(paper):
    paper *= 2


l = [1, 2]
duplicate(l)

print(l)