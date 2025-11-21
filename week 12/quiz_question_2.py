import math
class Point:
    def __init__(self, x_coord, y_coord):
        self.x = x_coord
        self.y = y_coord
    
    def __eq__(self, otherpoint):
        return self.x == otherpoint.x and self.y == otherpoint.y
    
    def distance(self, otherpoint):
        return math.sqrt((self.x - otherpoint.x)**2 + (self.y - otherpoint.y)**2)
    
    def __str__(self):
        return f"({self.x}, {self.y})"
    
point1 = Point(3,4)
point2 = Point(3,4)
print(point1 == point2)
print(point1.distance(point2))