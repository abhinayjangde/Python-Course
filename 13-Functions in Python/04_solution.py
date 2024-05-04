import math

def area(radius):
    a = math.pi*radius**2
    c = 2*math.pi*radius
    return a,c 

print(area(4))