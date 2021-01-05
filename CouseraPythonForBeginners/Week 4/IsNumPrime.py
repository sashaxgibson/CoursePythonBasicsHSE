from math import sqrt
from math import ceil
n = int(input())


def IsPrime(n):
    if n == 2:
        return True
    x = ceil(sqrt(n))
    while x > 1:
        if n % x == 0:
            return False
        else:
            x -= 1
            continue
    return True


if IsPrime(n) is False:
    print("NO")
else:
    print("YES")
