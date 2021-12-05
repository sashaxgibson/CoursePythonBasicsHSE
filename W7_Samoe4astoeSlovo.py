inFile = open('input.txt')
a = inFile.read().split()
slavear = dict()
for cur in a:
    if cur in slavear:
        slavear[cur] += 1
    else:
        slavear[cur] = 1
print(slavear)
#answList = sorted(slavear, key=lambda x: (slavear[x], x))
#print(answList[0])
for cur in slavear:
    print(-slavear[cur], cur)
