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

m = Matrix([[1, 0], [0, 1]]).size()
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]]).size()
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]]).size()
print(m)
