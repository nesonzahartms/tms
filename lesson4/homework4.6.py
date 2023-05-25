
dict_1 = {"key1": 1, "key2": 2,  "key3": 3, "key4": 4, "key5": 5}
print(dict_1)

dict_2 = dict(zip(dict_1.values(), dict_1.keys()))
print(dict_2)