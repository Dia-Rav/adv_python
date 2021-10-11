import complex

class Complex:
    def __init__(self, re = 0, im = 0):
        self.__re = re
        self.__im = im  
    def __add__ (self, other):
        return Complex(self.__re+other.__re, self.__im+other.__im)
    def __sub__(self, other):
        return Complex(self.__re-other.__re, self.__im-other.__im)
    def __mul__(self, other):
        return Complex(self.__re*other.__re - self.__im*other.__im , self.__im*other.__re + self.__re*other.__im)
    def __truediv__(self, other):
        if other.__im**2 + other.__re**2 == 0:
            return
        temp = Complex((self.__re*other.__re+self.__im*other.__im)/(other.__im**2 + other.__re**2) , (self.__im*other.__re - self.__re*other.__im)/(other.__im**2 + other.__re**2))
        return temp
    def __abs__(self):
        return (self.__re**2 + self.__im**2)**(1/2)
    def __str__(self):
        return f'({self.__re}+{self.__im}j)' if self.__im >= 0 \
          else f'({self.__re}{self.__im}j)'
    def real(self):
        return self.__re
    def imag(self):
        return self.__im
    def __eq__(self, other):
        return self.__re == other.__re and self.__im == other.__im
help (complex)
a = 2 + 3j
b = 5 + 4j
c = Complex(2, 3)
d = Complex(5, 4)
print (a+b)
print (c+d)
print (a-b)
print (c-d)
print (a*b)
print (c*d)
print (abs(c))
print (abs(a))

