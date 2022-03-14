price = float(input())
rublz = int(price)
copeks = float('{0:.2f}'.format(price - rublz)) * 100
print(rublz, int(copeks))
