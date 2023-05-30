#
# from random import randint
#
# min = int(input('Минимум: '))
# max = int(input('Максимум: '))
# qty = int(input('Количество элементов: '))
#
# lst = [randint(min, max) for i in range(qty)]
#
# s = set(lst)
# for i in s:
#     print(f"'{i}': {lst.count(i)}")

from random import randint
def fill_list(minimum, maximum, amount, empty_list):
    for i in range(amount):
        empty_list.append(randint(minimum, maximum))


def analysis(from_list, to_dict):
    for i in from_list:
        if i in to_dict:
            to_dict[i] += 1
        else:
            to_dict[i] = 1


lst = []
dct = {}

min = int(input('Минимум: '))
max = int(input('Максимум: '))
qty = int(input('Количество элементов: '))

fill_list(min, max, qty, lst)
analysis(lst, dct)

for item in sorted(dct):
    print(f"'{item}': {dct[item]}")


