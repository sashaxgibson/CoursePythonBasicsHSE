inFile = open('input.txt')
a = inFile.read().split()
slavear = dict()
for cur in a:
    if cur in slavear:
        slavear[cur] += 1
    else:
        slavear[cur] = 1
answList = []
for i in slavear:
    answList.append((slavear[i], i))
answList.sort(key=lambda i: (-i[0], i[1]))
for i in answList:
    print(i[1])
