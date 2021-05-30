#K = int(input())
K = 5
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
print(lines)
N = len(lines)
myScoreList = []
for now in lines:
    x = now.split()
    tempMan = (int(x[-3]), int(x[-2]), int(x[-1]))
    myScoreList.append(tempMan)
print(myScoreList)
print(sum(myScoreList[0]))
