import time


def prime_numbers(n):
    lst = [1, 2]
    for i in range(3, n+1, 2):
        if (i > 10) and not(i % 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if (i % j == 0):
                break
        else:
            lst.append(i)
    return lst


start_time = time.time()

print(prime_numbers(60))

print(time.time() - start_time)
