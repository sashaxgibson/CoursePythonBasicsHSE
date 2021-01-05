from math import floor, ceil
a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
dtr = a * d - b * c
dtr1 = e * d - b * f
dtr2 = a * f - c * e
x = dtr1 / dtr
y = dtr2 / dtr
FractPart = float('{0:.6f}'.format(x - int(x)))
if FractPart == 0:
    x = int(x)
else:
    x = '{0:.6f}'.format(x)

FractPart = float('{0:.6f}'.format(y - int(y)))
if FractPart == 0:
    y = int(y)
else:
    y = '{0:.6f}'.format(y)
print(x, y)
