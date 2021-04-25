inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
nameList = inFile.readlines()
answList = []
for i in range(len(nameList)):
    a = nameList[i].split()
    answList.append(a[0] + ' ' + a[1] + ' ' + a[3] + '\n')
answList.sort()
print(''.join(answList), file=outFile)
inFile.close()
outFile.close()
