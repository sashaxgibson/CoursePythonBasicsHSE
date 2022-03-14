from math import sqrt
n = int(input())


def MinDivisor(n):
    x = 1
    while x <= sqrt(n):
        x += 1
        if n % x == 0:
            return x


x = MinDivisor(n)
if x is None:
    print(n)
else:
    print(x)
