from math import sqrt

class SpecialRelativity:

    def __init__(self,v):
        self.v = v # Velocity
        self.c = 3e8 # speed of causalty
        self.k = sqrt(1-self.v**2/self.c**2) # Lorentz factor
        
    def lorentz_factor(self):
        return round(self.k,3)

class TimeDilation(SpecialRelativity):

    def __init__(self, v, t_0):
        super().__init__(v)
        self.t_0 = t_0 # Proper time 
        
    def t_dil(self):
        t = self.t_0/self.k 
        return round(t,5)

class LengthContraction(SpecialRelativity):

    def __init__(self,v,l_0):
        super().__init__(v)
        self.l_0 = l_0 # Proper length
        
    def l_cont(self):
        l = self.l_0*self.k
        return round(l,5)

class MassIncrease(SpecialRelativity):

    def __init__(self,v,m_0):
        super().__init__(v)
        self.m_0 = m_0 # Rest mass
        
    def mass_inc(self):
        m = self.m_0/self.k
        return round(m,5)        

event1 = TimeDilation(2e8,4)
event2 = LengthContraction(2e7,5.2)
event3 = MassIncrease(2.7e8,50)

print(event1.lorentz_factor())
print(event1.t_dil())
print(event2.l_cont())
print(event3.mass_inc())
