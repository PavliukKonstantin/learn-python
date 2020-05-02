# В этой практике вы будете реализовывать функции для работы с множествами,
# как с наборами флагов.
#
# Флаги удобны для управления работой некоторого кода: если флаг поднят,
# значит какая-то возможность включена.
# В этом плане флаги похожи на галочки в формах и бланках — галочку тоже
# можно поставить или не поставить.
#
# В нашем случае флаги будут представлять собой элементы множества: если
# элемент в множестве присутствует,
# значит и флаг поднят. Вам же нужно будет реализовать две функции:
# toggle и toggled.
#
# Функция toggle
# Эта функция должна принимать флаг (один!) и множество в качестве аргументов.
# Если флаг уже присутствует в множестве,
# его нужно из множества убрать. Если же флаг отсутствует,
# то его нужно добавить. Таким образом функция будет
# переключать состояние флага. Множество нужно заменять "по месту",
# возвращать из функции ничего не нужно.
# Пример использования функции toggle:
#
# READ_ONLY = 'read_only'
# flags = set()
# toggle(READ_ONLY, flags)
# READ_ONLY in flags
# True
# toggle(READ_ONLY, flags)
# READ_ONLY in flags
# False
# Функция toggled
# Эта функция работает похожим на toggle образом,
# но вместо изменения исходного множества возвращает новое
# — с уже переключенным флагом. Пример:
#
# READ_ONLY = 'read_only'
# flags = set()
# new_flags = toggled(READ_ONLY, flags)
# READ_ONLY in flags
# False
# READ_ONLY in new_flags
# True


def toggle(key, source):
    source.discard(key) if key in source else source.add(key)


# READ_ONLY = 'read_only'
# flags = set()
# toggle(READ_ONLY, flags)
# toggle(READ_ONLY, flags)
# print(flags)
# print(READ_ONLY in flags)


def toggled(key, source):
    result = source.copy()
    result.discard(key) if key in result else result.add(key)
    return result


# READ_ONLY = 'read_only'
# flags = set()
# new_flags = toggled(READ_ONLY, flags)
# print(flags)
# print(READ_ONLY in flags)
# print(new_flags)
# print(READ_ONLY in new_flags)


def test_toggle():
    a, b = "ab"
    flags = set()
    result = toggle(a, flags)
    assert result is None, "Should not return anything!"
    assert flags == {a}
    toggle(b, flags)
    assert flags == {a, b}
    toggle(a, flags)
    assert flags == {b}
    toggle(b, flags)
    assert not flags


def test_toggle_ints():
    a, b = (42, 100)
    flags = set()
    result = toggle(a, flags)
    assert result is None, "Should not return anything!"
    assert flags == {a}
    toggle(b, flags)
    assert flags == {a, b}
    toggle(a, flags)
    assert flags == {b}
    toggle(b, flags)
    assert not flags


def test_toggled():
    a, b, c = "abc"
    flags = {a, b}
    assert toggled(c, flags) is not flags, "Should return a new set!"
    assert flags == {a, b}, "Old set should not be changed!"
    assert c in toggled(c, flags)
    assert b not in toggled(b, flags)


def test_roundtrip_toggle():
    a, b, c = "abc"
    flags = {a, b}
    toggle(c, flags)
    toggle(c, flags)
    assert flags == {a, b}


def test_roundtrip_toggled():
    a, b, c = 1, 2, 3
    flags = {a, b}
    assert toggled(c, toggled(c, flags)) == flags


test_roundtrip_toggle()
test_toggle()
test_toggle_ints()
test_toggled()
test_roundtrip_toggled()
