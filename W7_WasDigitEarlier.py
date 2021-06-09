a = list(map(int, input().split()))
emptySet = set()
i = 0
while i < len(a):
    if a[i] in emptySet:
        print("YES")
    else:
        print("NO")
    emptySet.add(a[i])
    i += 1
