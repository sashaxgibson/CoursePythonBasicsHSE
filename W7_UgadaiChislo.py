##Ctrl + D чтобы остановить ввод в sys.stdin
import sys
a = list(sys.stdin.readlines())
print(a)
print(int(a[0]) * 3)
##print(' '.join((a[0] * 3).split()))