a = list(map(int, input().split()))
min = a[0]
pmin = 0
max = a[0]
pmax = 0
for i in range(len(a)):
    if a[i] < min:
        min = a[i]
        pmin = i
for i in range(len(a)):
    if a[i] > max:
        max = a[i]
        pmax = i
a[pmin], a[pmax] = a[pmax], a[pmin]
print(*a)
