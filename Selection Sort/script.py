# Selection Sort
# by n3nz 13/01/19

import random

ValArr =  []    # Массив
ArrSize = 10    # Размер
Counter = 0     # Счетчик

# Заполнение массива случайными числами
while Counter < ArrSize:
    ValArr.append(random.randrange(0,100))
    Counter += 1

# Алгоритм сортировки
#    По возрастанию

i = 0
e = 0

for i, e in enumerate(ValArr):
        mn = min(range(i, len(ValArr)), key=ValArr.__getitem__)
        ValArr[i] = ValArr[mn] 
        ValArr[mn] = e

print(ValArr)