name="Abhi"
age=22 # global variable
def f1():
    age=20 # local variable
    print(age)

# f1()
# print(age)

def f2():
    global age
    age=50 
    print(age)
f2()
print(age)


