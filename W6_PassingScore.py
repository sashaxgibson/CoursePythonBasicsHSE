inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
K = int(inFile.readline())
lines = inFile.readlines()
myScoreList = []
for now in lines:
    x = now.split()
    curManScore = (int(x[-3]), int(x[-2]), int(x[-1]))
    myScoreList.append(curManScore)
goodScoreList = []
for now in myScoreList:
    if now[0] > 39 and now[1] > 39 and now[2] > 39:
        goodScoreList.append(sum(now))
    else:
        continue
goodScoreList.sort(reverse=True)
if len(goodScoreList) <= K:
        print(0, file=outFile)
else:
    if goodScoreList[0] == goodScoreList[K]:
        print(1, file=outFile)
    else:

inFile.close()
outFile.close()
