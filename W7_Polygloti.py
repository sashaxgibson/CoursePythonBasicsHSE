inFile = open('input.txt', 'r', encoding='utf-8')
dataList = []
for line in inFile:
    dataList.append(line.strip())
print(dataList)
i = 1
curQuanLang = int(dataList[i])
tstList = dataList[i + 1:i + 1 + curQuanLang]
print(tstList)
i = 1
while i < len(dataList):
