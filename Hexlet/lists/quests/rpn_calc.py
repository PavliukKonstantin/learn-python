# В данном упражнении необходимо реализовать стековую машину,
# то есть алгоритм, проводящий вычисления по обратной польской записи.
#
# Обратная польская нотация или постфиксная нотация — форма записи математических и логических выражений,
# в которой операнды расположены перед знаками операций. Выражение читается слева направо.
# Когда в выражении встречается знак операции, выполняется соответствующая операция над двумя ближайшими операндами,
# находящимися слева от знака операции. Результат операции заменяет в выражении последовательность её операндов и знак,
# после чего выражение вычисляется дальше по тому же правилу. Таким образом,
# результатом вычисления всего выражения становится результат последней вычисленной операции.
#
# Например, выражение (1 + 2) * 4 + 3 в постфиксной нотации будет выглядеть так: 1 2 + 4 * 3 +,
# а результат вычисления: 15. Другой пример - выражение: 7 - 2 * 3, в постфиксной нотации: 7 2 3 * -, результат: 1.

# Реализуйте функцию rpn_calc, которая принимает список,
# каждый элемент которого содержит число или знак операции (+, -, *, /).
# Функция должна вернуть результат вычисления по обратной польской записи.

# import operator
#
# get_operator = {
#     '+': operator.add,
#     '-': operator.sub,
#     '*': operator.mul,
#     '/': operator.truediv,
# }.get
#
#
# def rpn_calc(rpn):
#     stack = []
#     for elem in rpn:
#         op = get_operator(elem)
#         if op is not None:
#             x = stack.pop()
#             y = stack.pop()
#             elem = op(y, x)
#         stack.append(elem)
#     return stack[0]


def rpn_calc(rpn):
    def oper_def(operator: str, num1, num2):
        operators = {
            '+': lambda x, y: x + y,
            '-': lambda x, y: x - y,
            '*': lambda x, y: x * y,
            '/': lambda x, y: x / y,
        }
        return operators[operator](num1, num2)

    while len(rpn) > 1:
        for index, item in enumerate(rpn):
            temp_list = []
            if isinstance(item, str):
                temp_list.extend(rpn[:index - 2])
                temp_list.append(oper_def(rpn[index], rpn[index - 2], rpn[index - 1]))
                temp_list.extend(rpn[index + 1:])
                rpn = temp_list
                break
    return rpn[0]


def test_rpn_calc():
    assert rpn_calc([1, 2, '+', 4, '*', 3, '+']) == 15
    assert rpn_calc([7, 2, 3, '*', '-']) == 1
    assert rpn_calc([1, 2, '+', 2, '*']) == 6


test_rpn_calc()
