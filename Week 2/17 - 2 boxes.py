A1, B1, C1 = int(input()), int(input()), int(input())
A2, B2, C2 = int(input()), int(input()), int(input())
if not A1 <= B1 <= C1 and A1 > B1:
    A1, B1 = B1, A1
if not A1 <= B1 <= C1 and B1 > C1:
    B1, C1 = C1, B1
if not A1 <= B1 <= C1 and A1 > B1:
    A1, B1 = B1, A1
if not A2 <= B2 <= C2 and A2 > B2:
    A2, B2 = B2, A2
if not A2 <= B2 <= C2 and B2 > C2:
    B2, C2 = C2, B2
if not A2 <= B2 <= C2 and A2 > B2:
    A2, B2 = B2, A2

if A1 == A2 and B1 == B2 and C1 == C2:
    print("Boxes are equal")
elif A1 >= A2 and B1 >= B2 and C1 >= C2:
    print("The first box is larger than the second one")
elif A2 >= A1 and B2 >= B1 and C2 >= C1:
    print("The first box is smaller than the second one")
else:
    print("Boxes are incomparable")
