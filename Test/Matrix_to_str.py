basedList = [[10, 10, 10], [11, 11, 11], [12, 12, 12]]
uni_lst = []
for i in basedList:
        uni_lst.append('\t'.join(map(str, i)))
print('\n'.join(map(str, uni_lst)))
