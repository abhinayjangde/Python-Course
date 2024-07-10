class Car:
    def __init__(self,brand=None,model=None):
        self.brand=brand
        self.model=model
        
    def getBrand(self):
        return self.brand
    def show(self):
        print(self.brand,self.model)
class Driver:
    def __init__(self,driverName=None):
        self.driverName=driverName

    def getDriverName(self):
        return self.driverName
    def setDriverName(self,dName):
        self.driverName=dName

class ElectricCar(Car,Driver):
    def __init__(self,brand,model,battery):
        super().__init__(brand,model)
        self.battery=battery
    def show(self):
        print(self.brand,self.model,self.battery)

c1 = Car("Toyota","X342")
c2 = ElectricCar("Tesla", "ERT2","34kph")
c2.setDriverName("Abhi")
c1.show()
c2.show()
# print(c2.getDriverName())

# print(isinstance(c2,ElectricCar))
# print(isinstance(c1,Car))