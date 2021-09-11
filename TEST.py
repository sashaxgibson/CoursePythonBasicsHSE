#' '.join(s.split())
a = 'benis \n'
print(' '.join(a.split()))
inFile = open('input.txt', 'r', encoding='utf8')
outFile = open('output.txt', 'w', encoding='utf8')
#nameList = inFile.readlines()
#print(nameList)
fuf = inFile.read()
print(fuf)
#Метод strip() применяется для удаления символа \n в конце введенных строк