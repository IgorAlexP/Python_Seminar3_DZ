"""
Задача 16: Требуется вычислить, сколько раз встречается некоторое число X
в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
N – количество элементов в массиве. В последующих строках записаны N целых чисел Ai.
Последняя строка содержит число X
n = 5
1 2 3 4 5
x = 3
-> 1
"""
count = 0
n = int(input("Введите размер списка: "))
list_1 = list(range(1, n+1))
x = int(input("Введите число x: "))
for i in list_1:
    if i == x:
        count = count + 1
print(f'n = {n}')
print(*list_1)
print(f'x = {x}')
print(f'-> {count}')