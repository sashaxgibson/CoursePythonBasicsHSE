i = int(input())
n = list(map(int, input().split()))
j = int(input())
m = list(map(int, input().split()))
nn = []
for i in range(len(n)):
    temptuple = (n[i], i + 1)
    nn.append(temptuple)
mm = []
for j in range(len(m)):
    temptuple = (m[j], j + 1)
    mm.append(temptuple)
nn.sort()
mm.sort()
j = 0
a = []
for i in range(len(nn)):
    while j < len(mm):
        dist = abs(nn[i][0] - mm[j][0])
        if j != len(mm) - 1:
            if dist <= abs(nn[i][0] - mm[j + 1][0]):
                a.append((mm[j][1], nn[i][1]))
                break
            if dist > abs(nn[i][0] - mm[j + 1][0]):
                j += 1
                continue
        if j == len(mm) - 1:
            a.append((mm[j][1], nn[i][1]))
            break


def reqOrder(a):
    return a[1]

a.sort(key=reqOrder)
answ = []
for i in range(len(a)):
    answ.append(a[i][0])
print(*answ)
