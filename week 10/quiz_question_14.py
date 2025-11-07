import math
class Circle:
    def __init__(self):
        self.radius = 0

    def get_radius(self):
        return self.radius
    def set_radius(self, value):
        self.radius = value
    
    def calculate_circumference(self):
        circumference = 2 * math.pi * self.radius
        return circumference
    def __str__(self):
        return f" The circumference of this cricle is: {self.calculate_circumference()}"

circle1 = Circle()
circle1.set_radius (4)

print (circle1)