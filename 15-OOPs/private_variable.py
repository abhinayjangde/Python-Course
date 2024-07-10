class Car:
    def __init__(self,brand=None,model=None):
        self.__brand=brand
        self.model=model
        
    def getBrand(self):
        return self.__brand
c = Car("Toyota","X342")
print(c.getBrand())