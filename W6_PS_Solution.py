K = 3
scoreList = [250, 200, 200, 200, 150, 150]
if K >= len(scoreList):
    print(0)
else:
    print(scoreList[K - 1])
    if scoreList[0] == scoreList[K - 1]:
        print(1)
    else:
        print(scoreList[K - 1])
