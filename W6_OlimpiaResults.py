N = int(input())
dataList = []
for i in range(N):
    tempManData = input().split()
    manData = (tempManData[0], int(tempManData[1]))
    dataList.append(manData)
dataList.sort(key=lambda x: x[1], reverse=True)
for i in range(len(dataList)):
    print(dataList[i][0])
while N != 0:
    a = input().split()
    dataList.append(a)
    N -= 1
print(dataList)
