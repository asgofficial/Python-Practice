import math


class Triangle:

    # Constructor
    def __init__(self, side1, side2, side3, angle1, angle2, angle3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self.angle1 = angle1
        self.angle2 = angle2
        self.angle3 = angle3

    # Find the target angle
    def findAngle(self):
        print("Angle 1:", self.angle1)
        print("Angle 2:", self.angle2)
        print("Angle 3:", self.angle3)


class EquilateralTriangle(Triangle):

    # Calculate area of equilateral triangle
    def calArea(self):
        area = (math.sqrt(3) / 4) * self.side1 ** 2
        print("Area of Equilateral Triangle:", round(area))


class Scalene(Triangle):

    # Calculate perimeter
    def calPerimeter(self):
        perimeter = self.side1 + self.side2 + self.side3
        print("Perimeter of Scalene Triangle:", perimeter)

    # Calculate area using Heron's formula
    def calArea(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(
            s * (s - self.side1) *
            (s - self.side2) *
            (s - self.side3)
        )

        print("Area of Scalene Triangle:", round(area))


# Equilateral Triangle object
e1 = EquilateralTriangle(6, 6, 6, 60, 60, 60)

print("EQUILATERAL TRIANGLE")
e1.findAngle()
e1.calArea()


# Scalene Triangle object
s1 = Scalene(5, 6, 7, 40, 60, 80)

print("\nSCALENE TRIANGLE")
s1.findAngle()
s1.calPerimeter()
s1.calArea()