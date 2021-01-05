s = str(input())
pos = s.find(' ')
w1 = s[:pos]
w2 = s[(pos + 1):]
print(w2 + ' ' + w1)
