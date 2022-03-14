a, b, c = int(input()), int(input()), int((input()))
if a == b and b == c:
    print(3)
elif a != b and a != c and b != c:
    print(0)
elif (a == b and b != c) or (a == c and c != b) or (c == b and a != b):
    print(2)
