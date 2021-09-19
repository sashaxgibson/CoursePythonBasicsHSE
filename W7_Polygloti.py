inFile = open('input.txt', 'r', encoding='utf8')
dataList = inFile.readlines()
N = int(dataList[0])
allLang = set()
comLang = set()
i = 1
while i <= N + 1:
    curLangQ = int(dataList[i])
