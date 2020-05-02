# Реализуйте функцию find_where, которая принимает на вход список книг
# и поисковый запрос и возвращает первую книгу,
# которая соответствует запросу. Каждая книга в списке — это словарь,
# содержащий её параметры,
# поисковый запрос — тоже словарь с параметрами.
#
# Если совпадений не было, то функция должна вернуть None.

# def find_where(items, search_request):
#     # Значение object() в качестве умолчательного используется для того,
#     # чтобы не получилось получить от get значение None и случайно
#     # успешно сравнить с value == None.
#     # Каждое значение object() всегда равно только самому себе.
#     default = object()
#     for item in items:
#         for key, value in search_request.items():
#             # Здесь можно было бы использовать
#             # что-то вроде "key in book and book[key] !=..." и обойтись
#             # без всяких object(). Но хочется обращаться по ключу
#             # ровно один раз!
#             if item.get(key, default) != value:
#                 break
#         else:
#             return item


def find_where(books_dict, search_query: dict) -> dict:
    set_search_query = set(search_query.items())
    for book in books_dict:
        if set_search_query.issubset(set(book.items())):
            return book


TITLE, AUTHOR, YEAR = 'title', 'author', 'year'
BOOKS = (
    {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111},
    {TITLE: 'Cymbeline', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'The Tempest', AUTHOR: 'Shakespeare', YEAR: 1611},
    {TITLE: 'Book of Foos Barrrs', AUTHOR: 'FooBar', YEAR: 2222},
    {TITLE: 'Still foooing', AUTHOR: 'FooBar', YEAR: 333},
    {TITLE: 'Happy Foo', AUTHOR: 'FooBar', YEAR: 4444},
)


def test_find_where():
    assert find_where(BOOKS, {}) == BOOKS[0]

    assert find_where(BOOKS, {AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {YEAR: 1111, AUTHOR: 'Pushkin'}) is None

    assert find_where(BOOKS, {"genre": 'Thriller'}) is None

    assert find_where(
        BOOKS, {YEAR: 1111},
    ) == {TITLE: 'Book of Fooos', AUTHOR: 'Foo', YEAR: 1111}

    assert find_where(
        BOOKS, {AUTHOR: 'Shakespeare', YEAR: 1611},
    )[TITLE] == 'Cymbeline'

    assert find_where(BOOKS, BOOKS[2]) == BOOKS[2]


test_find_where()
