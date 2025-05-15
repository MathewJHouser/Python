import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = float(x)
        self.__y = float(y)

    def getx(self):
        return float(self.__x)

    def gety(self):
        return float(self.__y)

    def distance_from_xy(self, x, y):
        dx = x - self.__x
        dy = y - self.__y
        return math.hypot(abs(dx), abs(dy))

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        total = 0
        total += self.__vertices[0].distance_from_point(self.__vertices[1])
        total += self.__vertices[1].distance_from_point(self.__vertices[2])
        total += self.__vertices[2].distance_from_point(self.__vertices[0])
        return total


triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
