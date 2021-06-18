inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
wordsSet = set()
allLines = inFile.readlines()
print(allLines)
for cur in allLines:
    tempLine = cur[:-3]
    print(tempLine)
    tempSet = set(tempLine)
    tempSet | wordsSet
    print(wordsSet)
