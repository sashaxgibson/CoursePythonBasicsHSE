inFile = open('input.txt', 'r', encoding='utf8')
demoList = inFile.read()
print(demoList)
dataList = inFile.readlines()
print(dataList)
clrList = []
for cur in dataList:
    clrList.append(cur.strip())
print(clrList)
