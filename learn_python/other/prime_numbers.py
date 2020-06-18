from datetime import datetime


def prime_numbers(n):
    lst = [1, 2]
    for i in range(3, n+1, 2):
        if not(i % 5) and (i > 10):
            continue
        for j in lst[2:]:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst


start_time = datetime.now()

print(prime_numbers(100))

print(datetime.now() - start_time)
