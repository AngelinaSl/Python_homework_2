# Задайте список из n чисел последовательности (1 + 1/n)^n и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06


number = int(input('Введите число: '))
my_list = []
for i in range(1, number + 1):
    my_list.append(round(((1 + 1/i)**i), 3))
print(my_list, end=' ')

print(f'Сумма = {round(sum(my_list), 3)}')