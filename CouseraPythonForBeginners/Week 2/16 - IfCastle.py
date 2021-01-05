A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())
case1 = ((A <= E and B <= D) or (A <= D and B <= E))
case2 = ((C <= E and B <= D) or (C <= D and B <= E))
case3 = ((A <= E and C <= D) or (A <= D and C <= E))
if case1 or case2 or case3 is True:
    print("YES")
else:
    print("NO")
