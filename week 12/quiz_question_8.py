class Rectangle:
    def __init__(self, width, height):
        self.w = width
        self.h = height
    def area(self):
        return self.w * self.h

    def __mul__(self, n):
        self.w *= n
        self.h *= n
        return self
    def __str__(self):
        return f'Rectangle ({self.w} X {self.h})'
r1 = Rectangle(4,5)
r1 * 3
print(r1)
print("Area", r1.area())