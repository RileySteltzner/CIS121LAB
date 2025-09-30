import math

def volume_cone(r,h):
    V = math.pi * ((r**2)*h)/3
    return V
print(volume_cone(3,3))