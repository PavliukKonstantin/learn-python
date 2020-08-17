# Написать функцию поиска четных чисел фибоначчи
def fib(n):
    if n <= 0:
        return "Enter a positive number"
    a = 0
    b = 1
    numbers = ["0"]
    for _ in range(n-1):
        for _ in range(3):
            a, b = b, a + b
        numbers.append(str(a))
    return ",".join(numbers)
