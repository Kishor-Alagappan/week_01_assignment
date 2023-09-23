class Rectangle:
    def __init__(self, leng, wid):
        self.leng = leng
        self.wid = wid
    def area(self):
        return self.leng * self.wid
    def perimeter(self):
        return 2 * (self.leng + self.wid)
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)

rectangle = Rectangle(8, 5)
square = Square(6)
print("Rectangle Area:", rectangle.area())
print("Rectangle Perimeter:", rectangle.perimeter())
print("Square Area:", square.area())
print("Square Perimeter:", square.perimeter())
