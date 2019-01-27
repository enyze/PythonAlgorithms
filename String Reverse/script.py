usword = "Hello, world!"
word = list(usword)

j = len(word)-1
i = 0
while i < j:
    temp = word[i]
    word[i] = word[j]
    word[j] = temp
    i, j = i + 1, j - 1

print(*word, sep = '')