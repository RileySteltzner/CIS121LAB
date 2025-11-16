class Vector:
    def __init__(self, x_component, y_component):
        self.x = x_component
        self.y = y_component
    
    def __eq__(self, othervector):
        return self.x == othervector.x and self.y == othervector.y
    
    def __str__(self):
        return f"{self.x}, {self.y}"
    
vector1 = Vector(3,5)
vector2 = Vector(3,5)
print(vector1 == vector2)
