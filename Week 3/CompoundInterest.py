p = int(input())
rub = int(input())
kop = int(input())
year = int(input())
Factor = float('{0:.6f}'.format(p / 100))
KopDepSum = kop + rub * 100
ProfSum = KopDepSum
while year >= 1:
    ProfSum += ProfSum * Factor
    ProfSum = int(ProfSum)
    year -= 1
print(ProfSum // 100, ProfSum % 100)
