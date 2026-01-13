from random import randint

number = randint(1, 100)
print('Угадайте число от 1 до 100')

while True:
    guess_number = int(input('Введите число: '))

    if guess_number < number:
        print('Ваше число меньше того, что загадано.')
    elif guess_number > number:
        print('Ваше число боьше того, что загадано.')
    elif guess_number == number:
        break
print('Отличная интуиция! Вы угадали число :)')