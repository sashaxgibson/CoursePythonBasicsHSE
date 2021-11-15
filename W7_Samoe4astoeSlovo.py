inFile = open('input.txt')
a = inFile.read().split()
slavear = dict()
for cur in a:
    if cur in slavear:
        slavear[cur] += 1
    else:
        slavear[cur] = 1
print(slavear)
for i in slavear:
    print(i, slavear[i])
