x = float(input())
y = float(input())


def IsPointInSquare(x, y):
    answ = -1 <= x <= 1 and -1 <= y <= 1
    return answ


if IsPointInSquare(x, y) is True:
    print("YES")
else:
    print("NO")
