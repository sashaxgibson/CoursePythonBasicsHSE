inFile = open('input.txt')
a = inFile.read()
wrdList = a.split()
knigga = dict()
for i in wrdList:
    if i in knigga:
        print(knigga[i], end=' ')
        knigga[i] += 1
    else:
        print(0, end=' ')
        knigga[i] = 1
