import os
#Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
""" n= int(input('Введите количество элементов первого множества: '))
m= int(input('Введите количество элементов второго множества: '))

list_n = []
list_m = []

list_nm = []
a = 0
print('Введите элементы первого множества: ')
while a != n:
       list_n.append(int(input()))
       a += 1

a = 0
print('Введите элементы второго множества: ')
while a != m:
        list_m.append(int(input()))
        a += 1
os.system('clear')

print('--------------------------------------')
print(n,end=' ')
print(m)
for i in list_n:
    print(i,end=' ')
print()
for i in list_m:
    print(i, end=' ')
print()
    
for i in list_n:
    for j in list_m:
        if i == j:
            list_nm.append(j)
            
list_nm = set(list_nm)
for i in sorted(list_nm):
    print(i,end=' ')
print() """

#Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растёт на круглой грядке, 
# причём кусты высажены только по окружности. 
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растёт N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод — 
# на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из 
# управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь 
# непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий 
# модуль, находясь перед некоторым кустом заданной во входном файле грядки.

# num = int(input('Введите количество кустов: '))
# list_num = []

# print("Введите количество ягод на кустах:")
# for i in range(num):
#     a = int(input())
#     list_num.append(a)
# os.system('clear')
# for i in list_num:
#     print(i, end=' ')
# print()
# list_sum = []

# for i in range(len(list_num)-1):
#     list_sum.append(list_num[i-1]+list_num[i]+list_num[i+1])
# list_sum.append(list_num[-2]+list_num[-1]+list_num[0])

# print(max(list_sum))