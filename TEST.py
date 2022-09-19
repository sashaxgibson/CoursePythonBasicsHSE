from sys import stdin
from copy import deepcopy


class Matrix:

    def __init__(self, listoflists):
        self.obj_list = deepcopy(listoflists)

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
                result_line.append(self.obj_list[i][j] + second_mtrx.obj_list[i][j])
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


m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1 + m2)
