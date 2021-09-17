inFile = open('input.txt', 'r', encoding='utf8')
dataList = inFile.readlines()
N = int(dataList[0])
allLang = set()
comLang = set()
for i in range(N):
