# Parent class:
class CarBrands:

    def __init__(self,model,engine,acceleration,topspeed):
        self.model = model
        self.engine = engine
        self.acceleration = acceleration
        self.topspeed = topspeed    

# Child class:
class Porsche(CarBrands):

    def __init__(self, model, engine, acceleration, topspeed):
        super().__init__(model, engine, acceleration, topspeed)
        self.est =  1948 # a property of the child class

    def info(self):
        print("First model (356) produced in",self.est)
        print("Model = ",self.model)
        print("Engine = ",self.engine)
        print("Acceleration (0-100kph) = ",self.acceleration)
        print("Top speed (kph) = ",self.topspeed)

# Another child class:
class Nissan(CarBrands):
    def __init__(self, model, engine, acceleration, topspeed):
        super().__init__(model, engine, acceleration, topspeed)
        self.est = 1933

    def info(self):
        print("Established in",self.est)
        print("Model = ",self.model)
        print("Engine = ",self.engine)
        print("Acceleration (0-60mph) = ",self.acceleration)
        print("Top speed (mph) = ",self.topspeed)

# Instances:    
car1 = Porsche("917LH","Flat-12","~2.3seconds","~383kph")
car2 = Nissan("Skyline GTR R34","RB26DETT (276bhp)","5.6s","160mph")

print("-------------------------")
car1.info()
print("-------------------------")
car2.info()
print("-------------------------")
