inFile = open('input.txt', 'r', encoding='UTF-8')
outFile = open('output.txt', 'w', encoding='UTF-8')
dataList = []
dataDict = dict()
for i in inFile:
    if i in dataDict:
        dataDict[i] += 1
    else:
        dataDict[i] = 1
for i in dataDict:
    dataList.append((dataDict[i], str(i).strip()))
votesSum = 0
for i in dataList:
    votesSum += i[0]
dataList.sort(key=lambda x: (-x[0], x[1]))
for now in dataList:
    if now[0] > votesSum / 2:
        print(now[1], file=outFile)
        break
    else:
        print(dataList[0][1], file=outFile)
        print(dataList[1][1], file=outFile)
        break
