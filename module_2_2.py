print("Введите последовательно три целых числа:")
first = int(input('Введите первое число: '))
second = int(input('Введите второе число: '))
third = int(input('Введите третье число: '))

if first == second and first == third:
    print('Количество равных чисел: 3')
elif first == second or first == third or second == third:
    print('Количество равных чисел: 2')
else:
    print('Количество равных чисел: 0')
