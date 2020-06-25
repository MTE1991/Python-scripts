class Temperature:

    def __init__(self,t):
        self.t = t
        
    def celsius_to_fahrenheight(self):
        f = (self.t)/5 + 32
        return round(f,2)

    def celsius_to_kelvin(self):
        k = self.t + 273
        return round(k,2)

    def fahrenheight_to_celsius(self):
        c = 5*(self.t-32)/9
        return round(c,2)

    def fahrenheight_to_kelvin(self):
        k = 5*(self.t-32)/9 + 273
        return round(k,2)

    def kelvin_to_celsius(self):
        c = self.t - 273
        return round(c,2)

    def kelvin_to_fahrenheight(self):
        f = 9*(self.t)/5 + 32            
        return round(f,2)

t1 = Temperature(32)
print(t1.celsius_to_kelvin())        