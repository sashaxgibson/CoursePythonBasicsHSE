p = int(input())
rub = int(input())
kop = int(input())
Factor = float('{0:.6f}'.format(p / 100))
KopDepSum = kop + rub * 100
profit = int(KopDepSum) * Factor
Sum = KopDepSum + int(profit)
print(Sum // 100, Sum % 100)
