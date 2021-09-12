#import sys
#dataList = list(sys.stdin.readlines())
inFile = open('input.txt', 'r', encoding='utf8')
dataList = inFile.readlines()
print(dataList)
baseSet = set(range(1, int(dataList[0]) + 1))
print(baseSet)
for i in range(1, len(dataList) + 1, 2):
    if dataList[i].strip() != 'HELP':
        beatSet = set(dataList[i].split())
        if dataList[i + 1] == 'YES':
            continue
        if dataList[i + 1] == 'NO':
            beatSet = set(int(dataList[i]))
            baseSet = baseSet - beatSet
    else:
        print(sorted(list(baseSet)))
