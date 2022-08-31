import functools
print(functools.reduce(lambda x, y: x * y, map(lambda x: pow(int(x), 5), input().split())))
