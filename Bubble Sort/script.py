# Bubble sort
# by n3nz 13/01/19

import random

ValArr =  []    # Массив
ArrSize = 3    # Размер
Counter = 0     # Счетчик
Swap = True     # Проверка свапа значений

# Заполнение массива случайными числами
while Counter < ArrSize:
    ValArr.append(random.randrange(0,100))
    Counter += 1

# Алгоритм сортировки
#    По возрастанию

NoP = 0        # Количество проходов 
Element = 0    # Номер текущего элемента

print(ValArr) 

for NoP in range(ArrSize):                      # Перебор всего массива от 0 до size
    Swap = False                                # Сброс проверки свапа
    for Element in range((ArrSize-1) - NoP):    # Перебор от 0 до Size - номер текущего прохода
        if ValArr[Element] > ValArr[Element+1]: # Если текущий элемент больше следующего
            ValArr[Element+1], ValArr[Element] = ValArr[Element], ValArr[Element+1] # Свап
            Swap = True                         # Произошел свап
    if not Swap: break                          # Если свапа не было, закончить сортировку

print(ValArr)