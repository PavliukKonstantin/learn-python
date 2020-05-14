# Реализуйте абстракцию для работы с URL.
# Она должна извлекать и менять части адреса.
#
# Интерфейс:
#
# make(url) - Конструктор. Создает URL.
# get_scheme(data) - Селектор (геттер). Извлекает схему.
# set_scheme(data, scheme) - Сеттер. Меняет схему.
# get_host(data) - Геттер. Извлекает host.
# set_host(data, host) - Сеттер. Меняет host.
# get_path(data) - Геттер. Извлекает путь.
# set_path(data, path) - Сеттер. Меняет путь.
# get_query_param(data, param_name, default=None) - Геттер.
# Извлекает значение для параметра запроса.
# Третьим параметром функция принимает значение по умолчанию,
# которое возвращается тогда, когда в запросе не было такого параметра
# set_query_param(data, key, value) - Сеттер.
# Устанавливает значение для параметра запроса.
# Если передано значение None, то параметр отбрасывается.
# to_string(data) - Геттер. Преобразует URL в строковой вид.
# Все сеттеры должны возвращать новый изменённый URL,
# а старый оставлять неизменным.
#
# Примеры
# >>> import url
# >>> u = url.make('https://hexlet.io/community?q=low')
# >>>
# >>> u = url.set_scheme(u, 'http')
# >>> url.to_string(u)
# 'http://hexlet.io/community?q=low'
# >>>
# >>> u = url.set_path(u, '/404')
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=low'
# >>>
# >>> url.get_query_param(u, 'q')
# 'low'
# >>>
# >>> u = url.set_query_param(u, 'page', 5)
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=low&page=5'
# >>>
# >>> u = url.set_query_param(u, 'q', 'high')
# >>> url.to_string(u)
# 'http://hexlet.io/404?q=high&page=5'
# >>>
# >>> u = url.set_query_param(u, 'q', None)
# >>> url.to_string(u)
# 'http://hexlet.io/404?page=5'
#
# Подсказки
# Парсинг URL — urllib.parse.urlparse
# Парсинг параметров запроса — urllib.parse.parse_qs
# Формирование строки с параметрами запроса — urllib.parse.urlencode
# Сборка конечного URL — urllib.parse.urlunparse
# urlparse возвращает иммутабельный объект типа namedtuple.
# Получить копию такого объекта с одним изменённым значением можно
# с помощью метода _replace.
from urllib import parse


def make(url: str):
    return parse.urlparse(url)


def get_scheme(data):
    return data.scheme


def set_scheme(data, scheme):
    return data._replace(scheme=scheme)


def get_host(data):
    return data.netloc


def set_host(data, host):
    return data._replace(netloc=host)


def get_path(data):
    return data.path


def set_path(data, path):
    return data._replace(path=path)


def get_query_param(data, param_name, default=None):
    query = parse.parse_qs(data.query)
    if query.get(param_name) is None:
        return default
    return query[param_name][0]


def set_query_param(data, key, value):
    query = parse.parse_qs(data.query)
    query[key] = value
    if query.get(key) is None:
        query.pop(key)
    query_str = parse.urlencode(query, doseq=True)
    return data._replace(query=query_str)


def to_string(data):
    return parse.urlunparse(data)


# u = make('https://hexlet.io/community?q=low')
# print(u)
#
# print(get_scheme(u))
#
# print(set_scheme(u, 'http'))
#
# print(set_path(u, '/404'))
#
# print(get_query_param(u, 'q'))
#
# print(set_query_param(u, 'page', 5))
# print(set_query_param(u, 'q', 'high'))
# print(set_query_param(u, 'q', None))
#
# print(to_string(u))
