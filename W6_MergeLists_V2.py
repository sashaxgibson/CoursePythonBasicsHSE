def merge(a, b):
    c = []
    i = 0
    j = 0
    while i < len(a) and j < len(b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        elif a[i] == b[j]:
            c.append(a[i])
            i += 1
            c.append(b[j])
            j += 1
        else:
            c.append(b[j])
            j += 1
    if i == len(a):
        while j < len(b):
            c.append(b[j])
            j += 1
    elif j == len(b):
        while i < len(a):
            c.append(a[i])
            i += 1
    return c


a = list(map(int, input().split()))
b = list(map(int, input().split()))
answ = merge(a, b)
print(*answ)
