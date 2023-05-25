
import random

numb = 0

print('Привет, как тебя зовут?')
name = input()

number = random.randint(1, 10)
print('Ok ,' + name + ', Я загадал число от 1 до 10.')

for numb in range(7):
    print('Отгадай за 7 попытки!')
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Это число маленькое')

    if guess > number:
        print('Это число большое')

    if guess == number:
        break

if guess == number:
    numb = str(numb + 1)
    print('Отлично, ' + name + '! Я загадал ' + numb + ' поздравляю')

if guess != number:
    number = str(number)
    print('Эх, ты не справился к сожалению, это число ' + number + '.')