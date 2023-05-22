#Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, 
#Вам стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое. 
#Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг от друга пробелами. 
#Стихотворение  Винни-Пух вбивает в программу с клавиатуры. 
#В ответе напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не в порядке

'''S
def count_vowels(word):
    vowels = "aeiouyаеёиоуыэюя"
    count = 0
    for letter in word:
        if letter.lower() in vowels:
            count += 1
    return count

def check_rhythm(poem):
    words = poem.split()
    syllables = [count_vowels(word) for word in words]
    if len(set(syllables)) == 1:
        return "Парам пам-пам"
    else:
        return "Пам парам"

poem = input("Введите стихотворение Винни-Пуха: ")
print(check_rhythm(poem))
'''

#Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, 
#вычисляющую элемент по номеру строки и столбца.
#Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
#Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). 
#print_operation_table(multiply)

def print_operation_table(operation, num_rows=6, num_columns=6):
    for i in range(1, num_rows + 1):
        for j in range(1, num_columns + 1):
            print(operation(i, j), end="\t")
        print()

def multiply(i, j):
    return i * j
print_operation_table(multiply)