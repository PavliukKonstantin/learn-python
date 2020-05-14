from datetime import datetime
from collections import Counter
from random import randint

# n = int(input())
# a = [int(i) for i in input().split()]

a = [randint(1, 1000) for _ in range(100000)]

start_time = datetime.now()

counter = Counter(a)

print(counter.most_common(10))

result, max_count = list(counter.items())[0]
for number, count in counter.items():
    if count > max_count or (count == max_count and number > result):
        result = number
        max_count = count

print("Больше всех встречается ->", result)
print("Встречается", max_count, "раз")

print(datetime.now() - start_time)
