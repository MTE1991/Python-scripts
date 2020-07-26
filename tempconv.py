class Temperature:

    def __init__(self,t,unit):
        self.t = t
        self.unit = unit
        
    def celsius_to_fahrenheight(self):
        if self.unit == "c":
            f = 9*(self.t)/5 + 32
            return round(f,2)
        else:
            raise ValueError("Wrong Unit.")
        
    def celsius_to_kelvin(self):
        if self.unit == "c":
            k = self.t + 273
            return round(k,2)
        else:
            raise ValueError("Wrong Unit.")    

    def fahrenheight_to_celsius(self):
        if self.unit == "f":
            c = 5*(self.t-32)/9
            return round(c,2)
        else:
            raise ValueError("Wrong Unit.")
        

    def fahrenheight_to_kelvin(self):
        if self.unit == "f":
            k = 5*(self.t-32)/9 + 273
            return round(k,2)
        else:
            raise ValueError("Wrong Unit.")

    def kelvin_to_celsius(self):
        if self.unit == "k":
            c = self.t - 273
            return round(c,2)
        else:
            raise ValueError("Wrong Unit.")

    def kelvin_to_fahrenheight(self):
        if self.unit == "k":
            f = 9*(self.t)/5 + 32            
            return round(f,2)
        else:
            raise ValueError("Wrong Unit.")

t1 = Temperature(32,'c')
print(t1.celsius_to_kelvin()) 
