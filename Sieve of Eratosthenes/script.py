# Решето Эратосфена – это алгоритм нахождения простых чисел до заданного числа n.
# В процессе выполнения данного алгоритма постепенно отсеиваются составные числа, кратные простым, начиная с 2.

n = int(input("Вывод простых чисел до: "))
a = [0] * n # создание массива с n количеством элементов
# заполнение массива
for i in range(n):
    a[i] = i

# второй элемент - единица, которая не является простым числом.. сброс
a[1] = 0

m = 2   # замена на 0 начинается с 3-го элемента (первые 2 уже 0)
while m < n:    # перебор всех элементов до заданного числа
    if a[m] != 0:   # если элемент не 0 то
        j = m * 2   # увеличить в 2 раза(текущий элемент - простое число)
        while j < n:
            a[j] = 0    # сброс
            j = j + m   # перейти в позицию на m больше
    m += 1

# вывод простых чисел
b = []
for i in a:
    if a[i] != 0:
        b.append(a[i])

del a
print (b)