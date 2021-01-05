import math
a = float((input()))
b = float((input()))
c = float((input()))
P = (a + b + c) / 2
S = math.sqrt(P * (P - a) * (P - b) * (P - c))
print(S)
