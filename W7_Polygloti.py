inFile = open('input.txt', 'r', encoding='utf-8')
dataList = []
for line in inFile:
    dataList.append(line.strip())
print(dataList)
curQuanLang = int(dataList[1])
tstList = dataList[2:2+int(dataList[1])]
print(tstList)
