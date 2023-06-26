while True:
    s = input("Выберете операцию: сложение, вычитание, умножение, деление' (+, -, *, /): ")
    if s == '0':
        break
    if s not in ('+', '-', '*', '/'):
        continue
    a = float(input('Введите число: '))
    b = float(input('Введите число: '))

    if s == '+':
        print(a+b)
    elif s == '-':
        print(a-b)
    elif s == "*":
        print(a*b)
    elif s == "/":
        if b!=0:
            print(a/b)
        else:
            print("Делить на ноль нельзя")
