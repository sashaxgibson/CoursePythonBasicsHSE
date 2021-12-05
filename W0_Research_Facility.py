inFile = open('input.txt')
a = inFile.read().split()
slavear = dict()
for cur in a:
    if cur in slavear:
        slavear[cur] += 1
    else:
        slavear[cur] = 1
#print(slavear)
otvlist = []
for now in slavear:
    otvlist.append((now, slavear[now]))
    #print(otvlist[-1])
#print(sorted(otvlist, key=lambda x: (x[1], x[0]))[0])
slovo = sorted(otvlist, key=lambda x: (x[1], x[0]))[0]
print(slovo)
print(slovo[0])
