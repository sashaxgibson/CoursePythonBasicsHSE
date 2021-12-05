inFile = open('input.txt')
a = inFile.read().split()
slavear = dict()
for cur in a:
    if cur in slavear:
        slavear[cur] += 1
    else:
        slavear[cur] = 1
otvlist = []
for now in slavear:
    otvlist.append((now, -slavear[now]))
print((sorted(otvlist, key=lambda x: (x[1], x[0]))[0])[0])
