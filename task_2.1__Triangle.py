
class Shape:
    Height = 0
    Width = 0
    Area = 0
    def set_height(self,height):
        self.Height = height
        return self.Height
    def set_width(self, width):
        self.Width = width
        return self.Width
    def __init__(self, width, height):
        self.Height = height
        self.Width = width
        return 

class Triangle(Shape):
    def area (self):
        self.Area = self.Width*self.Height/2
        return self.Area

class Rectangle(Shape):
    def area (self):
        self.Area = self.Width*self.Height
        return self.Area

if __name__ == "__main__":
    Tri = Triangle(8, 6)
    Rec = Rectangle(8, 6)
    print (Tri)
    print (Tri.area())
    print (Rec.area())


