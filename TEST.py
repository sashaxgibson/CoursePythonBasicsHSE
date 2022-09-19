from copy import deepcopy

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
        for i in range(second_mtrx.size()):
            result_line = []
            for j in range(len(self.obj_list[0])):
                result_line.append(self.obj_list[i][j] + second_mtrx[i][j])
            result_mtrx.append(result_line)
        return Matrix(result_mtrx)

m1 = Matrix([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
m2 = Matrix([[0, 1, 0], [20, 0, -1], [-1, -2, 0]])
print(m1.size())
