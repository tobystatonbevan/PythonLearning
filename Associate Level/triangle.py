import math


class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        self.__distancex = x - self.__x
        self.__distancey = y - self.__y
        return math.hypot(self.__distancey,self.__distancex)

    def distance_from_point(self, point):
        self.__distancex = point.getx() - self.__x
        self.__distancey = point.gety() - self.__y
        return math.hypot(self.__distancey,self.__distancex)


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__threePoints = [vertice1,vertice2,vertice3]

    def perimeter(self):
        return self.__threePoints[0].distance_from_point(self.__threePoints[1])+self.__threePoints[1].distance_from_point(self.__threePoints[2])+self.__threePoints[2].distance_from_point(self.__threePoints[0])

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
    