from operator import eq
s = ("aba", "baba", "assa")
res = all(map(lambda x: eq(*x), zip(s, reversed(s))))
res1 = all(map(lambda x: not eq(*x), zip(s, reversed(s))))
print(res)
print(res1)