from math import sqrt
a = float(input())
b = float(input())
c = float(input())
D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-1 * b - sqrt(b ** 2 - 4 * a * c)) / 2 * a
    x2 = (-1 * b + sqrt(b ** 2 - 4 * a * c)) / 2 * a
    if '{0:.6f}'.format(x1) <= '{0:.6f}'.format(x2):
        print('{0:.6f}'.format(x1), '{0:.6f}'.format(x2))
    else:
        print('{0:.6f}'.format(x2), '{0:.6f}'.format(x1))
elif D == 0:
    x1 = (-1 * b) / 2 * a
    print('{0:.6f}'.format(x1))
