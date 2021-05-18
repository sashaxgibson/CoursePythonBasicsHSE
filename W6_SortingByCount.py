dataList = list(map(int, input().split()))


def countSort(dataList):
    countNumList = [0] * 101
    for cur in dataList:
        countNumList[cur] += 1
    answList = []
    for num in range(len(countNumList)):
        for i in range(countNumList[num]):
            answList.append(num)
    print(*answList)


countSort(dataList)
