from math import sqrt

class SpecialRelativity:
    def __init__(self,v,t_0,m_0,l_0):
        self.v = v # velocity
        self.t_0 = t_0 # Proper time 
        self.m_0 = m_0 # Rest mass
        self.l_0 = l_0 # Proper length
        self.c = 3e8 # speed of causalty
        self.k = sqrt(1-v**2/c**2) # Lorentz factor
        
class TimeDilation(SpecialRelativity):
    def __init__(self,v,t_0):
        super().__init__(v,t_0)
    
    def t_dil(self):
        t = t_0/k 
        return round(t,5)
        
