class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def __eq__(self, other):
        return self.a == other.a and self.b == other.b

    def __str__(self):
        sign = "+" if self.b >= 0 else "_"
        return f"{self.a} {sign} {abs(self.b)}i"

c1 = ComplexNumber(3,2)
c2 = ComplexNumber(3,2)
print(c1 == c2)
print("c1 =", c1)
print("c2 =", c2)