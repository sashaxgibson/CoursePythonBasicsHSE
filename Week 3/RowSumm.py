n = int((input()))
S = 0
while n >= 1:
    S += 1 / n ** 2
    n -= 1
print('{0:.6f}'.format(S))
