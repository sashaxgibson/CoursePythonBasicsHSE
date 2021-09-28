inFile = open('input.txt', 'r', encoding='utf-8')
dataList = []
for line in inFile:
    dataList.append(line.strip())
print(dataList)
