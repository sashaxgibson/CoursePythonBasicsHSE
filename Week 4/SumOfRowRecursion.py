def srr(sum):
    a = int(input())
    if a == 0:
        print(sum)
    if a != 0:
        sum = sum + a
        srr(sum)


sum = 0
srr(sum)
