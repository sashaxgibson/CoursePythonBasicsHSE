a = ['10\n', '1 2 3 4 5 6 7 8 9 10\n', 'YES\n', '1\n', 'NO\n', '2\n', 'NO\n', '3\n', 'NO\n', '4\n', 'NO\n', '6\n', 'NO\n', '7\n', 'NO\n', '8\n', 'NO\n', '9\n', 'NO\n', '10\n', 'NO\n', 'HELP\n']
#curNum = a[1].strip().split()
#print(curNum)
print(set(map(int, a[1].strip().split())))
curAnsw = a[2].strip()
print(curAnsw)
#import sys
#dataList = list(sys.stdin.readlines())