inFile = open('input.txt')
a = inFile.read().split()
slavear = dict()
for cur in a:
    if cur in slavear:
        slavear[cur] += 1
    else:
        slavear[cur] = 1
print(slavear)
listWrd = []
for i in slavear:
    print(i, slavear[i])
    listWrd.append((i, slavear[i]))
print(listWrd)
print(listWrd[2][0])
