from copy import deepcopy

basedList = [[10, 10, 10], [11, 11, 11], [12, 12, 12]]
cutList = basedList[:]
copiedList = deepcopy(basedList)
tstList = []
for i in basedList:
    tempList = []
    for j in i:
        tempList.append(j)
    tstList.append(tempList)
basedList[0][1] = 88
basedList[1][1] = 101
basedList[2][1] = 999
print('basedList', basedList)
print('cutList', cutList)
print('copiedList', copiedList)
print('tstList', tstList)
