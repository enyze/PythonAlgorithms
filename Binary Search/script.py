# Бинарный(двоичный) поиск // Binary search

arr = [0,45,67,32,12,36,87,93,16,52,11,20,28,30,0]  # Массив значений // Our array
x = 32  # Элемент в этом массиве

i = 0
j = len(arr)-1
m = int(j/2)

while arr[m] != x and i <= j:
    if x > arr[m]:
        i = m+1
    else:
        j = m-1
    m = int((i+j)/2)

if i >= j:
    print("Элемент не найден!")
else: 
    print("Индекс элемента: ", m)
