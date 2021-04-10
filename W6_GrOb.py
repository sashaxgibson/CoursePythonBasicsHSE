#i = int(input())
#n = list(map(int, input().split()))
#j = int(input())
#m = list(map(int, input().split()))
n = [79, 64, 13, 8, 38, 29, 58, 20, 56, 17]
m = [53, 19, 20, 85, 82, 39, 58, 46, 51, 69]
nn = []
temptuple = 0
for i in range(len(n)):
    temptuple = (n[i], i + 1)
    nn.append(temptuple)
mm = []
for j in range(len(m)):
    temptuple = (m[j], j + 1)
    mm.append(temptuple)
print(nn)
print(mm)
nn.sort()
mm.sort()
print(nn)
print(mm)
answList = []
j = 0
for i in range(len(nn)):
    while j <= len(mm) - 1:
        if j < len(mm):
            d1 = abs(nn[i][0] - mm[j][0])
            d2 = abs(nn[i][0] - mm[j + 1][0])
            if d1 < d2:
                answ = (nn[i][1], mm[j][1])
                answList.append(answ)
                break
            else:
                j += 1
                continue
        if j == len(mm) - 1:

answList.sort()
print(answList)
