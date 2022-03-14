n = 1
FirstNum = int(input())
SecondNum = int(input())
if SecondNum > FirstNum:
    SecondNum, FirstNum = FirstNum, SecondNum
while n != 0:
    n = int(input())
    if n < SecondNum:
        continue
    elif n > SecondNum and n > FirstNum:
        SecondNum, FirstNum = FirstNum, n
    elif n > SecondNum and n < FirstNum:
        SecondNum = n
    elif n == FirstNum:
        SecondNum = n
print(SecondNum)
