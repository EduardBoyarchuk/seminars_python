#Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai
#.Последняя строка содержит число X
""" import random  as rm
N = int(input('N = '))
list_one = [rm.randint(1,N) for i in range(1,N+1)]
print(list_one)

X = int(input('X = '))
count = 0
for i in list_one:
    if i == X:
        count +=1
print(count) """

# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# . Последняя строка
# содержит число X

""" import random  as rm
N = int(input('N = '))
list_number = [i for i in range(1,N+1)]
print(list_number)

X = int(input('X = '))

if X > N+1:
    print('Рядом ничего нет')
elif X<=-1:
    print('Рядом ничего нет')
elif X==0:
    print(list_number[X])
elif X==1:
    print(list_number[X])
elif X<=N+1:
    print(list_number[X-2]) """
    
#Задача 20: В настольной игре Скрабл (Scrabble) каждая буква имеет определенную
# ценность. В случае с английским алфавитом очки распределяются так:
# ● A, E, I, O, U, L, N, S, T, R – 1 очко;
# ● D, G – 2 очка;
# ● B, C, M, P – 3 очка;
# ● F, H, V, W, Y – 4 очка;
# ● K – 5 очков;
# ● J, X – 8 очков;
# ● Q, Z – 10 очков.
# А русские буквы оцениваются так:
# ● А, В, Е, И, Н, О, Р, С, Т – 1 очко;
# ● Д, К, Л, М, П, У – 2 очка;
# ● Б, Г, Ё, Ь, Я – 3 очка;
# ● Й, Ы – 4 очка;
# ● Ж, З, Х, Ц, Ч – 5 очков;
# ● Ш, Э, Ю – 8 очков;
# ● Ф, Щ, Ъ – 10 очков.
# Напишите программу, которая вычисляет стоимость введенного пользователем слова.
# Будем считать, что на вход подается только одно слово, которое содержит либо только
# английские, либо только русские буквы.
""" 
dict_en = {1: ['A','E','I','O','U','L','N','S','T','R'],
           2: ['D',2,'G'],
           3: ['B','C','M','P'],
           4: ['F','H','V','W','Y'],
           5: ['K'],
           8: ['J','X'],
          10: ['Q','Z']         
}
dict_ru = {1: ['А','В','Е','И','Н','О','Р','С','Т'],
           2: ['Д','К','Л','М','П','У'],
           3: ['Б','Г','Ё','Ь','Я'],
           4: ['Й','Ы'],
           5: ['Ж','З','Х','Ц','Ч'],
           8: ['Ш','Э','Ю'],
          10: ['Ф','Щ','Ъ']
    
}

value = input('Пиши слово: ')
value = value.upper()
vv = []


for d in value:
    for k, v in dict_en.items():
        for i in v:
            if i==d:
                vv.append(k)
                
for d in value:
    for k, v in dict_ru.items():
        for i in v:
            if i==d:
                vv.append(k)
print(sum(vv)) """