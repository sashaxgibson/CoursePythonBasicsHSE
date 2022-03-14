#'{0:.6f}'.format()
def power(a, n):
    if n == 0:
        return 1
    if n != 0:
        return '{0:.6f}'.format(a) * power(a, n - 1)


a = float(input())
n = int(input())
print(power(a, n))
