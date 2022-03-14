s = str(input())
d = len(s)
pos1 = s.find('f')
if pos1 != -1:
    s2 = s[:pos1:-1]
    pos2 = s2.find('f')
    if pos2 != -1:
        pos2 = d - pos2 - 1
        print(pos1, pos2)
    else:
        print(pos1)
