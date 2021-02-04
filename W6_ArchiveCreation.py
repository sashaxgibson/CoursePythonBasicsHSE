s, n = map(int, input().split())
memList = []
while n > 0:
    memList.append(int(input()))
    n -= 1
memList.sort()
i = 0
storVol = 0
while i < len(memList) and storVol + memList[i] < s:
    storVol = storVol + memList[i]
    i += 1
print(i)
