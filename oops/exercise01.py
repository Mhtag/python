class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, lenght):
        self.length = lenght
    def area(self):
        return self.length ** 2



rect1 = Shape()
rect2 = Square(5)

print(rect1.area())
print(rect2.area())

rect2.length = 9

print(rect2.area())
