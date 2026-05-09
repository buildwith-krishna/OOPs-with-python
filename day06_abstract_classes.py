from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        circle_area = math.pi*self.radius**2
        print(f"Area of the circle is: {circle_area}cm*2")

class Rectangle(Shape):
    def __init__(self, length, bridth):
        self.length = length
        self.bridth = bridth

    def area(self):

        area_rectangle = self.length*self.bridth
        print(f"Area of the rectangle is : {area_rectangle}cm*2")

class Triangle(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        area_triangle = 0.5*self.side**2
        print(f"Area of the equalitral traingle is : {area_triangle}cm*2")

radius = int(input("Enter radius: ").strip())
length = int(input("Enter length: ").strip())
bridth = int(input("Enter bridth: ").strip())
side = int(input("Enter side: ").strip())

c = Circle(radius)
r = Rectangle(length, bridth)
t = Triangle(side)

c.area() 
r.area()
t.area()
