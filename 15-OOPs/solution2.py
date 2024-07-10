class Circle:
    def __init__(self,radius=None):
        self.radius=radius

    def setRadius(self,r):
        self.radius=r
    def getRadius(self):
        return self.radius
    def getCircum(self):
        return 2 * 3.14 * self.radius
    def getArea(self):
        return 3.14 * self.radius * self.radius
c = Circle()
c.setRadius(5)
# print(c.getRadius())
print(c.getArea())
print(c.getCircum())