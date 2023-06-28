from random import random


class RandomValue:
    def __init__(self, ):
        self.value = []

    def __iter__(self):
        return RandomValueIterator(self.value)


class RandomValueIterator:
    def __init__(self, qty):
        self.qty = qty
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.qty > 0:
            self.cur += random()
            self.qty -= 1
            return round(self.cur, 1)
        else:
            raise StopIteration



my_limit = int(input("Введите лимит: "))
my_random = RandomValueIterator(my_limit)
for item in my_random:
    print(item)


results = [elem for elem in my_random]
print(results)

assert len(results) == my_limit
for i in results:
    assert i is not None
