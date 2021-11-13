inFile = open('input.txt')
N = int(inFile.readline())
slovar = {}
while N > 0:
    curline = inFile.readline()
    print(curline.split())
    N -= 1
