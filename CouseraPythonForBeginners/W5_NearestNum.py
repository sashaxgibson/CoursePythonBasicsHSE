N = int(input())
numList = list(map(int, input().split()))
x = int(input())
p = numList[0]
g = abs(x - numList[0])
for i in range(N):
    if abs(x - numList[i]) < g:
        g = abs(x - numList[i])
        p = numList[i]
print(p)
