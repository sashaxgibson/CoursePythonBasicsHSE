# insert(index, x)
# append
a = [1, 3, 3, 5, 7]  # i - номер элемента в массиве a
b = [-1, 0, 2, 4, 4, 5, 8]  # j - номер элемента в массиве b
print(a, b)
i = 0
while i < len(a):
    for j in range(len(b)):
        if b[j] <= a[i]:
            a.insert(i, b[j])
        if b[j] > a[i]:
            i += 1
            continue
        


print(a)
