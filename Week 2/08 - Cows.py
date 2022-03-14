n = int(input())
ln = n % 10
if ln == 1 and n != 11:
    print(n, "korova")
elif 2 <= ln <= 4 and 12 < n > 14 or 2 <= n <= 4:
    print(n, "korovy")
else:
    print(n, "korov")
