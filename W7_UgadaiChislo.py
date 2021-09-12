inFile = open('input.txt', 'r', encoding='utf8')
dataList = inFile.readlines()
baseSet = set(range(1, int(dataList[0]) + 1))
for i in range(1, len(dataList), 2):
    if dataList[i].strip() != 'HELP':
        curSet = set(map(int, dataList[i].strip().split()))
        curAnsw = dataList[i + 1].strip()
        if curAnsw == 'NO':
            baseSet -= curSet
            continue
        elif curAnsw == 'YES':
            baseSet &= curSet
            continue
    if dataList[i].strip() == 'HELP':
        print(*sorted(baseSet))
