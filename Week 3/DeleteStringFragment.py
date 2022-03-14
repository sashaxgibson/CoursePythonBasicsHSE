s = str(input())
d = len(s)
pos1 = s.find('h')
pos2 = d - (s[::-1].find('h')) - 1
s1 = s[:pos1]
s2 = s[(pos2 + 1):]
print(s1 + s2)
