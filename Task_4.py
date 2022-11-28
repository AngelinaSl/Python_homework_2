# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных индексах. Индексы вводятся одной строкой, через пробел.
# n = 3
# [-3, -2, -1, 0, 1, 2, 3] --> 0 2 3
# -3 * -1 * 0 = 0
# Вывод: 0

number = int(input('Введите число:'))
my_list = []
for i in range(-number, number + 1):
    my_list.append(i)
print(f"n = {number}: {my_list}")
string_index = input('Введите индексы чисел (через пробел), которые хотите перемножить: ')
list_index = string_index.split(' ')
new_list = [int(x) for x in list_index]
print(f"{my_list} --> ", end=" ")
print(*new_list)
mult = 1
k = 0
while k < len(new_list):
    mult *= my_list[new_list[k]]
    k += 1
print(f"Вывод: {mult}")
