# Линейный поиск

import random

ValArr = []
cnt = 0

while cnt < 1000:
    ValArr.append(random.randrange(0,100))
    cnt += 1

def FindThatInRange(arr, l, r, key):
    x = l
    for x in range(l,r):
        if arr[x] is key:
            print("Found! ", arr[x], " at position: ", x)

FindThatInRange(ValArr, 0, 1000, 13)