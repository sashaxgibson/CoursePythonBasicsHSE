from sys import stdin

class Matrix:


    def __init__(self, ListOfLists):
        tstList = []
        for i in ListOfLists:
            tempList = []
            for j in i:
                tempList.append(j)
            tstList.append(tempList)
        self.obj_list = tstList


    def __str__(self):
        for i in self:
            print(*map(str, i), sep='\t')
            return map(str, i)


    def size(self):
        return len(self.obj_list), len(self.obj_list[0])

