inFile = open('input.txt')
a = inFile.read().split()
print(a)
slavear = {}
for cur in a:
    if cur in slavear:
        slavear[cur] += 1
    else:
        slavear[cur] = 1
print(slavear)
print(*slavear.values())
for i in slavear:
    print(i)
print(slavear.va)