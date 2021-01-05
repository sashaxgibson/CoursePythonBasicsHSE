def rs():
    a = int(input())
    if a == 0:
        print(a)
    if a != 0:
        rs()
        print(a)


rs()
