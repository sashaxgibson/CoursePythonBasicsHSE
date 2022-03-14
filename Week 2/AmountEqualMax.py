n = int(input())
MaxNumber = n
qntt = 1
while n != 0:
    n = int(input())
    if n < MaxNumber:
        continue
    elif n > MaxNumber:
        qntt = 1
        MaxNumber = n
    elif n == MaxNumber:
        qntt += 1
print(qntt)
