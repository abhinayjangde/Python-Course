# print(name="Abhi") # throws an error
# print(name:="Abhi")
# a, *b, c = [1, 2, 3, 4, 5]
# print(a)
# print(b)
# print(c)

def greet(name,/, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet(name="Abhinay"))