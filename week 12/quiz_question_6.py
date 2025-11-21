class RGBColor:
    def __init__(self, r, g, b):
        self.r = min(max(r,0), 255)
        self.g = min(max(g,0), 255)
        self.b = min(max(b,0), 255)
    def __add__(self, other):
        new_r = min((self.r+other.r)//2, 255)
        new_g = min((self.g+other.g)//2, 255)
        new_b = min((self.b+other.b)//2, 255)
        return RGBColor(new_r, new_g, new_b)
    def __str__(self):
        return f"RGB ({self.r}, {self.g}, {self.b})"
    
c1 = RGBColor(170, 150, 200)
c2 = RGBColor(30, 10, 60)
c3 = c1 + c2
print(c3)