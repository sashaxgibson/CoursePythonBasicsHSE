from sys import stdin


class Matrix:

    def __init__(self, listoflists):
        tstlist = []
        for i in listoflists:
            templist = []
            for j in i:
                templist.append(j)
            tstlist.append(templist)
        self.obj_list = tstlist

    def __str__(self):
        uni_lst = []
        for i in self.obj_list:
            uni_lst.append('\t'.join(map(str, i)))
        return '\n'.join(map(str, uni_lst))

    def size(self):
        return len(self.obj_list), len(self.obj_list[0])

    def __add__(self, second_mtrx):
        result_mtrx = []
        for i in range(len(self.obj_list)):
            result_line = []
            for j in range(len(self.obj_list[0])):
                result_line.append(self.obj_list[i][j] + second_mtrx[i][j])
            result_mtrx.append(result_line)
        return Matrix(result_mtrx)

    def __mul__(self, mnozh):
        new_matrix = []
        for i in range(len(self.obj_list)):
            new_matrix_line = []
            for j in range(len(self.obj_list[0])):
                new_matrix_line.append(j * mnozh)
            new_matrix.append(new_matrix_line)
            return Matrix(new_matrix)

    __rmul__ = __mul__

exec(stdin.read())
