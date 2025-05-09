from random import randint

print('Задача 5. Игра «Угадай число»')

# Папа-программист любит придумывать для сына небольшие компьютерные игры.

# Напишите программу-игру, в которой один человек загадывает число от 1 до 10,
# а другой пытается его угадать.
# Программа должна запрашивать число у пользователя до тех пор, пока тот не угадает загаданное.
# После каждой попытки выводите подсказки, больше или меньше загаданного введённое число.
# Также после отгадки выводите количество попыток.


# Пример (загадали число 7)
# Введите число: 3
# Число меньше, чем нужно. Попробуйте ещё раз!
# Введите число: 10
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 8
# Число больше, чем нужно. Попробуйте ещё раз!
# Введите число: 7
# Вы угадали! Число попыток: 4
N = randint(1, 10)
count = 0
while True:
    number = int(input('Введите число: '))
    count += 1
    if number > N:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
        continue
    if number < N:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
        continue
    else:
        print(f'Вы угадали! Число попыток: {count}')
        break
