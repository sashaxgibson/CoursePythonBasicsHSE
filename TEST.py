#a = list(map(int, input().split()))
a = [10, 100, 1000, 10000, 2]
print(a)
b = 1
for i in a:
    b = b * i
print(b ** 5)
