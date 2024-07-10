class Person:
    x=3
    def __init__(self,name=None,email=None):
        self.name = name
        self.email = email

    def show(self):
        print("hello", self.name,self.email)
    
    @staticmethod
    def f2():
        print("Hello")
    
    @classmethod
    def f3(cls):
        print(cls.x)

p1=Person("Abhi","abhi@gmail.com")
p2=Person("Ankit","ankit@Qgmail.com")
# p1=Person("Preeti","preeti@gmail.com")
# p1.show()
# p2.show()
# p1.f2()
# p1.f3()
# Person.f2()
# print(Person.name,Person.email)
# Person.show()