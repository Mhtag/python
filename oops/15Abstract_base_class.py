from abc import ABCMeta, abstractmethod

class Shape(metaclass=ABCMeta):
    @abstractmethod
    def printarea(self):
        return 0

class Rectangle(Shape):
    type = 'Rectangle'
    sides = 4
    def __init__(self):
        self.lenght = 6
        self.breadth = 7

    def printarea(self):
        return self.lenght * self.breadth

rect1 = Rectangle()

print(rect1.printarea())