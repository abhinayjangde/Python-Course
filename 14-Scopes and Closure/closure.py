# def f3():
#     age=23
#     def f4():
#         print(age)
#     return f4
# myfun = f3()
# myfun()

def f5(num):
    def helper(x):
        return x ** num
    return helper

square = f5(2)
cube = f5(3)
print(square(2))
print(cube(2))
