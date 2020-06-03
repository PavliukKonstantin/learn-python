from datetime import datetime
from random import randint

test = [randint(1, 1000) for _ in range(1000000)]

start_time = datetime.now()

a = max(set(test), key=test.count)
print("Больше всех встречается ->", a)
print("Встречается", test.count(a), "раз")

print(datetime.now() - start_time)
