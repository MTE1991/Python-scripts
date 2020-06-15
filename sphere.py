from math import pi

class Sphere: 
    def __init__(self,radius): # Initialization...
       self.r = radius # attribute(s)

    def area(self):
        a = 4*pi*self.r**2
        return round(a,4)

    def volume(self):
        v = (4/3)*pi*self.r**3
        return round(v,4)

s1 = Sphere(2)

print(s1.volume())