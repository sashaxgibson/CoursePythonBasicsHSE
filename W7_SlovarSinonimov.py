inFile = open('input.txt')
N = int(inFile.readline())
slovar = {}
while N > 0:
    curline = inFile.readline()
    templist = curline.split()
    slovar[templist[0]] = templist[1]
    slovar[templist[1]] = templist[0]
    N -= 1
askwrd = inFile.readline().strip()
print(slovar[askwrd])
