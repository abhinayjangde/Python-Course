class Person:
    def __init__(self,name,age):
        self.name=name
        self.age = age

    def show(self):
        print("Name", self.name)
        print("Age", self.age)

p = Person("Abhi",22)
p.show()