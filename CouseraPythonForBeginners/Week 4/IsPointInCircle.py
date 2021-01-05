from math import sqrt
x = float(input())
y = float(input())
xc = float(input())
yc = float(input())
r = float(input())


def IsPointInCircle(x, y, xc, yc, r):
    lenx = abs(x - xc)
    leny = abs(y - yc)
    veclen = sqrt(lenx ** 2 + leny ** 2)
    answ = veclen <= r
    return answ


if IsPointInCircle(x, y, xc, yc, r) is True:
    print("YES")
else:
    print("NO")
