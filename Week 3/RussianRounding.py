from math import floor, ceil
x = float(input())
AfterDot = x - int(x)
FractPart = float('{0:.6f}'.format(x - int(x)))
RequiredNum = int(FractPart * 10)
if RequiredNum >= 5:
    print(ceil(x))
else:
    print(floor(x))
