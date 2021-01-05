from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
epsilon = 10 ** 6
if D > 0:
    x1 = (-1 * b - sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    x2 = (-1 * b + sqrt(b ** 2 - 4 * a * c)) / (2 * a)
    if x1 == int(x1):
        x1 = int(x1)
    else:
        x1 = '{0:.6f}'.format(x1)
    if x2 == int(x2):
        x2 = int(x2)
    else:
        x2 = '{0:.6f}'.format(x2)
    if x1 <= x2:
        print(x1, x2)
    else:
        print(x2, x1)
elif D == 0:
    x1 = b / (2 * a) * -1
    if x1 == int(x1):
        x1 = int(x1)
    else:
        x1 = '{0:.6f}'.format(x1)
    print(x1)
