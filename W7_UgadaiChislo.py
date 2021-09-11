##Ctrl + D чтобы остановить ввод в sys.stdin
##print(' '.join(a[0].split()))
#import sys
#a = list(sys.stdin.readlines())
inFile = open('input.txt', 'r', encoding='utf8')
dataList = inFile.readlines()
print(dataList)
maxNum = int(dataList[0])
baseSet = set(range(1, maxNum + 1))
print(baseSet)
tempSet = set(list(map(int, dataList[1].split())))
answSet = set()
print(tempSet)
for i in range(3, len(dataList)):
    curSet = a[i - 1]
    if a[i].strip() == 'HELP':
        print(*answSet)
    else:
        if a[i].strip() == 'NO':
                continue
        if a[i].strip() == 'YES':
            answSet = tempSet - curSet

