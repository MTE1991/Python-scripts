class CarBrands:
    def __init__(self,model,engine,acceleration,topspeed):
        self.model = model
        self.engine = engine
        self.acceleration = acceleration
        self.topspeed = topspeed    

class Porsche(CarBrands):  
    def info(self):
        print("Model = ",self.model)
        print("Engine = ",self.engine)
        print("Acceleration (0-100kph) = ",self.acceleration)
        print("Top speed (kph) = ",self.topspeed)

class Nissan(CarBrands):
    def info(self):
        print("Model = ",self.model)
        print("Engine = ",self.engine)
        print("Acceleration (0-60mph) = ",self.acceleration)
        print("Top speed (mph) = ",self.topspeed)
    
car1 = Porsche("917LH","Flat-12","~2.3seconds","~383kph")
car2 = Nissan("Skyline GTR R34","RB26DETT (276bhp)","5.6s","160mph")

car1.info()
car2.info()