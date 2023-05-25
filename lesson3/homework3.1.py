# sentence1 = "Hi andrey"
# a = list(sentence1)
# a[0], a[1], a[4:9] = a[4:9], a[1], a[0]
# b = join(a)
# print(b)

print("1th way")
s = input("Введите имя и фамилию")
s1 = (s[round(len(s)-(len(s)//2)):])
s2 = (s[:(round(len(s)-len(s)//2))])
print(s1,s2)

# print("2th way")
# s = "neson zahar"
# l = s.split(' ')
# s = l[1] +' '+ l[0]
# print(s)
# s.split()
# ['neson', 'zahar']
# for word in s.split():
#     print(f'!{word}')
#     s1 = ' '.join(f'!{word}' for word in s.split())
#     print(s1)
#
# print("3th way")
# firstnam = input('Input your firstnam: ')
# lastnam = input('Input your lastnam: ')
# string_a = 'Hello, %s %s' % (lastnam + ' !', ' ' + firstnam)
# string_b = 'Hello, {} {}'.format(lastnam, firstnam)
# string_c = 'Hello, {0} {1}'.format(lastnam, firstnam)
# string_d = f'Hello, {lastnam}  {firstnam} '
# print(string_a)
# print(string_b)
# print(string_c)
# print(string_d)
