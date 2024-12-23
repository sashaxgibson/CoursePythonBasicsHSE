n = int(input())
m = int(input())
k = int(input())
if k > n * m:
    print("NO")
else:
    if ((n * m) - k) % n == 0 or ((n * m) - k) % m == 0:
        print("YES")
    else:
        print("NO")
