#Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
#Каждое число вводится с новой строки.
""" a1 = int(input("Введите первый элемент прогрессии: "))
d = int(input("Введите разницу прогрессии: "))
n = int(input("Введите количество элементов в прогрессии: "))

progression = []
for i in range(1, n+1):
    progression.append(a1 + (i-1) * d)

print("The arithmetic progression is:")
for num in progression:
    print(num) """

#Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)

arr = [-5, 9, 0, 3, -1, -2, 1,
        4, -2, 10, 2, 0, -9, 8, 10, -9,
        0, -5, -5, 7]
minimum = 5
maximum = 15

indexes = [i for i, x in enumerate(arr) if minimum <= x <= maximum]

print(indexes) # Output arr = [2, 5, 8, 10, 12, 15, 18]
minimum = 5
maximum = 15

indexes = [i for i, x in enumerate(arr) if minimum <= x <= maximum]

print(indexes) 