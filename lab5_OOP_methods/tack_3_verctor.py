class vector:

        
    def __add__ (self, other):
        return vector(self.x + other.x,
                      self.y + other.y,
                      self.z + other.z)

    def __sub__(self, other):
        return vector(self.x - other.x,
                      self.y - other.y,
                      self.z - other.z)

    def __mul__(self, other):
        return (self.x * other.x +
                self.y * other.y +
                self.z * other.z)**(1/2)
    def __truediv__(self, k):
        return vector(self.x / k,
                      self.y / k,
                      self.z / k)

    def __init__(self, *args):
        try:
            if type(args[0]) == str:
                args = [float(x) for x in args[0].split(',')]
        except IndexError:
            pass
        try:
            self.x, self.y, self.z = args[0], args[1], args[2]
        except IndexError:
            pass


    def __str__(self):
        return '[{}. {}. {}]'.format(self.x, self.y, self.z)
    def __matmul__(self, other):
        return vector(self.y*other.z-self.z*other.y,
                      self.x*other.z-self.z*other.x,
                      self.x*other.y-self.y*other.x)
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __abs__(self):
        return (self.x*self.x+self.y*self.y + self.z*self.z)**(1/2)

    def __gt__(self, other):
        return abs(self)>abs(other)

    def center_of_mass(n, vectors):
        sum = vector(0, 0, 0)
        for vect in vectors:
            vect = vector(vect)
            sum = sum + vect
        return sum/n
    def max_vector(n, vectors):
        max = vector(0, 0, 0)
        for vect in vectors:
            vect = vector(vect)
            if max<vect:
                max = vect
        return max
    def max_triangle_perimetr(n, vectors):
        max_perimetr = 0
        max_tri = None
        for i in range (n-2):
            for j in range (i+1, n-1):
                for k in range (j+1, n):
                    #такая сложная нумерация всего лишь исключает повторение рассматриваемых точек 
                    a = vector(vectors[i])
                    b = vector(vectors[j])
                    c = vector(vectors[k])
                    ab =abs(a-b)
                    ac = abs(a-c)
                    bc = abs(b-c)
                    perimetr = ac+ bc+ ab
                    if ab + ac> bc and ac + bc> ab and bc + ac> ab and perimetr>max_perimetr:
                        max_perimetr = perimetr
                        max_tri = [i, j, k]
        return max_tri
    def max_triangle_square (n, vectors):
        max_square = 0
        max_tri = None
        for i in range (n-2):
            for j in range (i+1, n-1):
                for k in range (j+1, n):
                    #такая сложная нумерация всего лишь исключает повторение рассматриваемых точек 
                    a = vector(vectors[i])
                    b = vector(vectors[j])
                    c = vector(vectors[k])
                    ab = a - b
                    ac = a - c
                    bc = b - c
                    square = abs((ab @ ac))/2
                    ab, ac, bc = map(abs, [ab, ac, bc])
                    if ab + ac> bc and ac + bc> ab and bc + ac> ab and square>max_square:
                        max_square = square
                        max_tri = [i, j, k]
        return max_tri

a = vector(1, 2, 3)
b = vector ('5, 4, 3')
print(a)
print(b)

print(f'Sum = {a + b}')
print(f'Dot product = {a * b}')
print(f'Cross product = {a @ b}')
#
N = int(input())
vectors = []
for i in range (N):
    vectors.append(input())
#я не смогла засунуть в список экземпляры класса
#пэтому приходится кадждый раз строки превращать в векторы
#я постараюсь это исправить 

print ('максимально удаленный вектор: ', vector.max_vector(N, vectors))
print ('центр масс: ', vector.center_of_mass(N, vectors))
print (f'площадь параллелограмма на векторах {a} и {b} : {abs(a @ b)}) '  )
max_triangle = vector.max_triangle_perimetr(N, vectors)
if max_triangle!= None:
    print ('максимальный треугольник по периметру: ')
    for temp in max_triangle:
        print (vectors[temp])
else:
    print ('невозможно составить треугольник')
max_triangle = vector.max_triangle_square(N, vectors)
if max_triangle!= None:
    print ('максимальный треугольник по площади: ')
    for temp in max_triangle:
        print (vectors[temp])
else:
    print ('невозможно составить треугольник')
'''
ввод:
10
1, 1, 1
0, 0, 0
2, 2, 2
3, 4, 5
6, 8, 9
10, 0, 2
4, 5, 6
3, 2, 1
1, 2, 3
10, 10, 10

вывод:
[1. 2. 3]
[5.0. 4.0. 3.0]
Sum = [6.0. 6.0. 6.0]
Dot product = 4.69041575982343
Cross product = [-6.0. -12.0. -6.0]
максимально удаленный вектор:  [10.0. 10.0. 10.0]
центр масс:  [4.0. 3.4. 3.9]
площадь параллелограмма на векторах [1. 2. 3] и [5.0. 4.0. 3.0] : 14.696938456699069)
максимальный треугольник по периметру:
0, 0, 0
10, 0, 2
10, 10, 10
максимальный треугольник по площади:
0, 0, 0
10, 0, 2
10, 10, 10
'''
