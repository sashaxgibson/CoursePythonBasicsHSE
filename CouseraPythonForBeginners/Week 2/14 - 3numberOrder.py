a, b, c = int(input()), int(input()), int(input())
if not a <= b <= c and a > b:
    a, b = b, a
if not a <= b <= c and b > c:
    b, c = c, b
if not a <= b <= c and a > b:
    a, b = b, a
print(a, b, c)
