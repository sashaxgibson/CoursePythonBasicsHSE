inFile = open('input.txt', 'r', encoding='utf8')
dataList = []
for line in inFile:
    dataList.append(line.strip())
print(dataList)
sumLang = set()
commonLang = set()
i = 0
while i < len(dataList):
    