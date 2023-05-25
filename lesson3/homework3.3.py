while True:
    name = input('Input your name:')
    age = input('Input your age:')
    age = int(age)
    while True:
        if age <= 0:
            print('Error, repeat input' ' ' + name)
        if 0 < age < 10:
            print('Hi Shket' ' ' + name)
        if 10 <= age <= 18:
            print('How your life' ' ' + name)
            if 18 < age <= 100:
                print('What you want?' ' ' + name)
else:
    print(name + ' ' 'You lie!')