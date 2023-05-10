from sys import stdin


class MatrixError(BaseException):
    def __init__(self, pervaja, vtoraja):
        self.matrix1 = pervaja
        self.matrix2 = vtoraja


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
        matrix_in = self.obj_list
        trdmatrix = []
        lines = len(matrix_in)
        columns = len(matrix_in[0])
        k = 0
        while k < columns:
            new_line = []
            for i in matrix_in:
                new_line.append(i[k])
            trdmatrix.append(new_line)
            k += 1
        self.obj_list = Matrix(trdmatrix)
        return self.obj_list

    @staticmethod
    def transposed(matrix_in):
        trdmatrix = []
        lines = len(matrix_in)
        columns = len(matrix_in[0])
        k = 0
        while k < columns:
            new_line = []
            for i in matrix_in:
                new_line.append(i[k])
            trdmatrix.append(new_line)
            k += 1
        return trdmatrix


#exec(stdin.read())

m = Matrix([[10, 10], [0, 0], [1, 1]])
print(m)
print(Matrix.transposed(m))
print(m)
