my_list = list(range(1, 101))

new_l = [x for x in my_list if x % 10 == 0]
print(new_l)

# new_l1 = [x if x % 4 != 0 else x*10 for x in my_list]
# print(new_l1)
