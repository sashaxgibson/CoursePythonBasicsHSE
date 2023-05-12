def transpose(list_in):
    trdMatrix = []
    for k in range(len(list_in[0])):
        new_line = []
        for i in list_in:
            new_line.append(i[k])
        trdMatrix.append(new_line)
    return trdMatrix


a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6]]
c = [[1, 8], [3, 7]]

print(*transpose(a))
print(*transpose(b))
print(*transpose(c))
