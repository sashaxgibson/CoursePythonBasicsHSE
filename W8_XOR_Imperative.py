import sys
#a = map(int, sys.stdin.readline().split())
#b = map(int, sys.stdin.readline().split())
a = [0, 0, 1, 1]
b = [0, 1, 0, 1]
#print(list(a), list(b))
#print(*zip(map(int, sys.stdin.readline().split()), map(int, sys.stdin.readline().split())))
#g = zip(a, b)
print(*map(lambda x: x[0] ^ x[1], zip(map(int, sys.stdin.readline().split()), map(int, sys.stdin.readline().split()))))
