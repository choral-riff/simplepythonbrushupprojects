"""
Problem Statement: Write a Python program that defines a Shape base class with an area() method, then implements it in Circle, Square, and Triangle subclasses using the appropriate geometric formulas.

Purpose: This exercise is a classic demonstration of polymorphism. Each shape shares the same area() interface but provides a completely different calculation, showing how OOP handles real-world variation cleanly.

Given Input: Circle(7), Square(4), Triangle(6, 8)

Expected Output:

Circle area: 153.94
Square area: 16
Triangle area: 24.0
"""
class Shape:
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius 
    
    def area(self):
        pi = 3.1415
        return self.radius*self.radius*pi 

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side*self.side

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def area(self):
        return 0.5*self.base*self.height

circ = Circle(7)
sq = Square(4)
tri = Triangle(6,8)

print(f"Circle area: {circ.area()}")
print(f"Square area: {sq.area()}")
print(f"Triangle area: {tri.area()}")
