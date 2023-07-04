from random import random

class RandomValue:
    def __init__(self):
        self.value = []

    def __iter__(self):
        qty = int(input("Введите лимит: "))
        cur = 0
        while qty > 0:
            cur += random()
            qty -= 1
            yield round(cur, 1)


my_random = RandomValue()
for item in my_random:
    print(item)

results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None