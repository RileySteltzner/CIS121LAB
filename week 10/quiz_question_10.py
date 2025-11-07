import math
class Vector:
    def __init__(self):
        self.x_direction = "unknown"
        self.y_direction = "unknown"
    def get_x_direction(self):
        return self.x_direction
    def set_x_direction(self, value):
        self.x_direction = value
    def get_y_direction(self):
        return self.y_direction
    def set_y_direction(self, value):
        self.y_direction = value
    
    def __str__ (self):
        magnitude = math.sqrt((self.x_direction)**2 + (self.y_direction)**2)
        return f"The vector magnitude is: {magnitude}"
vector1 = Vector()
vector1.set_x_direction(2)
vector1.set_y_direction(2)
print(vector1)