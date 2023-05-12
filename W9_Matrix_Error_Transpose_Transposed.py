from sys import stdin


class MatrixError(BaseException):
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2


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
        if self.size() == second_mtrx.size():
            result_mtrx = []
            for i in range(len(self.obj_list)):
                result_line = []
                for j in range(len(self.obj_list[0])):
                    x1 = self.obj_list[i][j]
                    x2 = second_mtrx.obj_list[i][j]
                    result_line.append(x1 + x2)
                result_mtrx.append(result_line)
        else:
            raise MatrixError(self, second_mtrx)
        return Matrix(result_mtrx)

    def __mul__(self, mnozh):
        new_matrix = []
        for i in range(len(self.obj_list)):
            new_matrix_line = []
            for j in range(len(self.obj_list[0])):
                xij = self.obj_list[i][j] * mnozh
                new_matrix_line.append(xij)
            new_matrix.append(new_matrix_line)
        return Matrix(new_matrix)

    __rmul__ = __mul__

    def transpose(self):
        t_matrix = []
        k = 0
        while k < len(self.obj_list[0]):
            new_line = []
            for i in self.obj_list:
                new_line.append(i[k])
            t_matrix.append(new_line)
            k += 1
        self.obj_list = t_matrix
        return self

    @staticmethod
    def transposed(matrix_in):
        trdMatrix = []
        for k in range(len(matrix_in.obj_list[0])):
            new_line = []
            for i in matrix_in.obj_list:
                new_line.append(i[k])
            trdMatrix.append(new_line)
        return Matrix(trdMatrix)


exec(stdin.read())
