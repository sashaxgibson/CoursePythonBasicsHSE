inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
nameList = inFile.readlines()
print(nameList)
a = nameList[0]
print(a)
print(a.strip())
