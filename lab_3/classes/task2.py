class Shape:
    def area(self):
        return 0


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        print(self.length * self.length)


ex1 = Shape()
print(ex1.area())

ex2 = Square(4)
ex2.area()
