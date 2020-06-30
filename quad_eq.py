from math import sqrt

class QuadraticEquation:
    def __init__(self,a,b,c):
        self.a = a # quadratic coefficient
        self.b = b # linear coefficient
        self.c = c # constant
        self.d = self.b**2 - 4*self.a*self.c # discriminant
    
    def roots(self):
        x1 = (-self.b + sqrt(self.d))/2*self.a
        x2 = (-self.b - sqrt(self.d))/2*self.a
        x = -self.b/2*self.a
        if self.d > 0:
            return x1, x2
        elif self.d == 0:
            return x

eq1 = QuadraticEquation(1,4,3)

print(eq1.roots())