def binary(number):
    result = ''
    if number == 0:
        result = '0'
    else:
        while number > 0:
            modulo = number % 2
            result = str(modulo) + result
            number = number // 2
    return result


print('string is -> ' + binary(101))
