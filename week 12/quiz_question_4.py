class LinearEquation:
    def __init__(self, m, b):
        self.m = m
        self.b = b
    def __add__(self, other):
        new_m = self.m + other.m
        new_b = self.b + other.b
        return LinearEquation(new_m, new_b)
    
    def __str__(self):
        sign = "+" if self.b >=0 else "-"
        return f"y = {self.m}x {sign} {abs(self.b)}"

le1 = LinearEquation(5,10)
le2 = LinearEquation(2,7)
print(le1)
print(le2)
le3 = le1.add(le2)
print(le3)