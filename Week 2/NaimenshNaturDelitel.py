x = int(input())
d = 2
while x % d != 0:
    d = d + 1
if x // d != 0:
    print(d)
