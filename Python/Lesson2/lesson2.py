# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

x = input("Введите вещественное число: ")
sum = 0

for i in x:
    if i == "." or i == "-":
        continue
    sum += int(i)

print(f"Сумма цифр: {sum}")

# 2. Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

n = int(input("Введите число N: "))
m = 1
array = []

for i in range (1, n+1):
    m *= i
    array.append(m)

print("Набор произведений чисел от 1 до N: " + str(array))

# 3. Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.
# Пример:
# - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

n = int(input("Введите число n: "))
list = [round((1 + 1/i)**i, 2) for i in range(1, n+1)]
print(list)

# Реализуйте алгоритм перемешивания списка.
import random

for i in range(len(list)-1, 0, -1):
    j = random.randint(0, i + 1) 
    list[i], list[j] = list[j], list[i] 
      
print ("Перемешанный список: " +  str(list))