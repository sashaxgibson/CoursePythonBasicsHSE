# index
# append
a = [1, 5, 7]  # i - номер элемента в массиве a
b = [-1, 0, 2, 4, 4, 5, 8]  # j - номер элемента в массиве b
print(a, b)
i = 0
while i < len(a):
    j = 0
    while j < len(b):
        if a[i] > b[j]:
            a.insert(i, b[j])
            i += 1
            continue
        if a[i] == b[j]:
            a.insert(i, b[j])
            i += 1
        if a[i] < b[j]:
            i += 1
            continue

    j += 1
print(a)
print(b)
