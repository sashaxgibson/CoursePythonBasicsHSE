class Complex:
    def __init__(self, re=0, im=0):
        self.re = re
        self.im = im

a = Complex(1, 2)
b = Complex(3)
c = Complex()
print(a.re, a.im)
print(b.re, b.im)
print(c.re, c.im)
