inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
dataStr = inFile.readlines()
dataList = []
for i in range(len(dataStr)):
    dataList.append(dataStr[i].split())
print(dataList)

def countSort(N):
    funcList = []
    for i in N:
        funcList[i] += 1
    print(funcList)


countSort(dataList)
