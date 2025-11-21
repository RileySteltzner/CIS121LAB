class RationalNumber:
    def __init__(self, numerator =1, denominator = 1):
        self.a = numerator
        self.b = denominator
    
    def __add__(self, otherFraction):
        new_numerator = 0
        new_denominator = 0
        if self.b == otherFraction.b:
            new_numerator = self.a + otherFraction.a
            new_denominator = self.b
        else:
            new_denominator = self.b * otherFraction.b
            new_numerator = (self.a * otherFraction.b) + (otherFraction.a * self.b)
        return RationalNumber(new_numerator,new_denominator)
    
    def __str__(self):
        return f"{self.a} / {self.b}"
fraction1 = RationalNumber(1, 3)
fraction2 = RationalNumber(1, 2)
fraction3 = fraction1 + fraction2
print(fraction3)