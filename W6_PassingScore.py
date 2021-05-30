#K = int(input())
K = 5
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
lines = inFile.readlines()
N = len(lines)
myScoreList = []
for now in lines:
    x = now.split()
    curManScore = (int(x[-3]), int(x[-2]), int(x[-1]))
    myScoreList.append(curManScore)
goodScoreList = []
for now in myScoreList:
    if now[0] and now[1] and now[2] >= 40:
        goodScoreList.append(sum(now))
    else:
        continue
goodScoreList.sort(reverse=True)
if len(goodScoreList) > K:
    answ = goodScoreList[4]
    print(answ)
elif len(goodScoreList) < K:
        print(0)
