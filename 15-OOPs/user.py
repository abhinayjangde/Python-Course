class User:

    def __init__(self,name=None,email=None):
        self.__name=name
        self.__email=email
    def show(self):
        print(self.__name, self.__email)

    @property
    def name(self):
        return self.__name

user1 = User("Abhi","abhi@gmail.com")
# user1.name = "ANkit"
print(user1.name)
