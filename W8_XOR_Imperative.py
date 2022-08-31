import sys
a = sys.stdin.readline().split()
b = sys.stdin.readline().split()
print(*zip(a, b))
