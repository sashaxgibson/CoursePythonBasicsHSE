inFile = open('input.txt', 'r', encoding='utf-8')
N = int(inFile.readline())
dataList = []
while N > 0:
    langNum = int(inFile.readline())
    tempList = []
    while langNum > 0:
        tempList.append(inFile.readline().strip())
        langNum -= 1
    dataList.append(tempList)
    N -= 1
comSet = set(dataList[0])
for now in dataList:
    comSet &= set(now)
print(len(comSet))
for x in comSet:
    print(x)
allSet = set()
for x in dataList:
    allSet |= set(x)
print(len(allSet))
for x in allSet:
    print(x)
