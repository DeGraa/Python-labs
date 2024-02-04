import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        return self.x, self.y

    def move(self, x, y):
        self.x = x
        self.y = y

    def dist(self, other_point):
        distance = math.sqrt(
            (self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2
        )
        return distance


point1 = Point(1, 2)
point2 = Point(3, 4)

print(point1.show())

print(point2.show())

distance = point1.dist(point2)
print(distance)
