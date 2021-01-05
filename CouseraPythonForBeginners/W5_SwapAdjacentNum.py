a = list(map(int, input().split()))
swap = len(a) // 2
stp = 1
i = 0
while stp <= swap:
    a[i], a[i + 1] = a[i + 1], a[i]
    i += 2
    stp += 1
print(*a)
