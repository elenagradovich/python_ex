'''
Сформировать одномерный список целых чисел A, используя генератор случайных чисел (диапазон от 0 до 99).
Размер списка n ввести с клавиатуры. В соответствии со своим вариантом написать программу по условию,
представленному в таблице ниже.
Для каждого четного по номеру элемента списка A найти его сумму со следующим элементом и записать эти суммы в новый список B.
'''

import random

n = int(input("Введите размер списка:\n"))
list_range = 99
a = []
for i in range(n):
    list_item = int(random.random() * list_range)
    a.append(list_item)
    print(list_item)
#-----------------------------------------
b = []

def is_even (index):
    return index % 2 == 0

print('New list: ')
for i in range(len(a)-1):
    if(is_even(i)):
        b.append(a[i] + a[i+1])

for i in range(len(b)):
    print(b[i])
