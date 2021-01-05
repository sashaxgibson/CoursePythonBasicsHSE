
a = float((input()))
b = float((input()))
c = float((input()))
P = (a + b + c) / 2
S = (P * (P - a) * (P - b) * (P - c)) ** (1 / 2)
print(S)
