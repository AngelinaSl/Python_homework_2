# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 0,56 -> 11

number = input('Введите число: ')
str_number = number.split(".")
integer = int(str_number[0])
fractional = int(str_number[1])
sum_numbers = 0
if integer != 0:
    while integer != 0:
        sum_numbers = sum_numbers + integer % 10
        integer //= 10
while fractional != 0:
    sum_numbers = sum_numbers + fractional % 10
    fractional //= 10
print(sum_numbers)
