n = int(input())
CurrentNum = n
OneRow = 1
TwoRow = 1
while n != 0:
    n = int(input())
    if n == 0:
        break
    elif n == CurrentNum:
        OneRow += 1
    elif n != CurrentNum:
        if OneRow > TwoRow:
            TwoRow = OneRow
            OneRow = 1
        else:
            OneRow = 1
        CurrentNum = n
if OneRow >= TwoRow:
    print(OneRow)
else:
    print(TwoRow)
