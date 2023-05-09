a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
b = [[1, 2, 3], [4, 5, 6]]

def transpose(matrix_in):
    trdMatrix = []
    lines = len(matrix_in)
    columns = len(matrix_in[0])
    k = 0
    while k < columns:
        new_line = []
        for i in matrix_in:
            new_line.append(i[k])
        trdMatrix.append(new_line)
        k += 1
    return trdMatrix

print(transpose(a))
print(transpose(b))
