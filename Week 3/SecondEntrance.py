s = str(input())
d = len(s)
pos1 = s.find('f')
if pos1 != -1:
    s1 = s[(pos1 + 1):]
    d1 = len(s1)
    pos2 = s1.find('f')
    if pos2 != -1:
        print(pos1 + (pos2 + 1))
    else:
        print(pos2)
else:
    print(-2)
