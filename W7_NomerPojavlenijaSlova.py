inFile = open('input.txt')
a = inFile.read()
wrdList = list(map(str, a.split()))
print(wrdList)
knigga = dict()
for i in wrdList:
    if i in knigga:
        print(knigga[i], end=' ')
    else:
        print(0, end=' ')
