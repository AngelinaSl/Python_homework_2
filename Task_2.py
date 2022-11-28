# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)


def factorial(x):
    if x == 1:
        return x
    else:
        return x * factorial(x - 1)


number = int(input("Введите число: "))
my_list = []
for i in range(1, number + 1):
    my_list.append(factorial(i))
print(f' N = {number} --> {my_list}')