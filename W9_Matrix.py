from sys import stdin

class Matrix:
    def __init__(self, x, y):
        self.x = x
        self.y = y


m = Matrix([[1, 0], [0, 1]])
print(m)
m = Matrix([[2, 0, 0], [0, 1, 10000]])
print(m)
m = Matrix([[-10, 20, 50, 2443], [-5235, 12, 4324, 4234]])
print(m)

#exec(stdin.read())
