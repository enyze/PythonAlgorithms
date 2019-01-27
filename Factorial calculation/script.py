# Вычисление факториала числа
n = int(input("Факториал числа: "))
fac = 1
i = 0

# 1) Реализация с помощью while
"""while i < n:
    i += 1
    fac = fac * i
print (" равен ", fac)"""

# 2) Реализация с помощью for
"""for i in range(1, n+1):
    fac *= i
print(" равен ", fac)"""

# 3) Реализация с помощью рекурсии
"""def fact(n):
    if n == 0:
        return 1
    return fact(n-1)*n
print(" равен ", fact(n))"""

# 4) Реализация с помощью функции factorial модуля math (только неотрицательные числа)
import math 
print(" равен ", math.factorial(n))
