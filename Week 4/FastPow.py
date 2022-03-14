def fastpow(a, n):
    if n <= 2:
        if n == 2:
            return a * fastpow(a, (n - 1))
        if n == 1:
            return a
        if n == 0:
            return 1
    if n > 2:
        if n % 2 == 0:
            a = a * a
            n = n // 2
            return fastpow(a, n)
        if n % 2 != 0:
            return a * fastpow(a, n - 1)


a = float(input())
n = int(input())
print('{0:.6f}'.format(fastpow(a, n)))
