import math

class Shape:
    def __init__(self, radius):
        self.radius = radius


class Circle(Shape):
    def calArea(self):
        area = math.pi * self.radius ** 2
        print("Area of Circle:", area)


class Sphere(Shape):
    def calVolume(self):
        volume = (4 / 3) * math.pi * self.radius ** 3
        print("Volume of Sphere:", volume)


c1 = Circle(5)
s1 = Sphere(5)

c1.calArea()
s1.calVolume()