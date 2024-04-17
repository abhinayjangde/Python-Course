# age = 18
age = int(input("Enter your age: "))
# print(type(age))

try:
    if age >= 18:
        print("You can vote!")
    else:
        print("You cannot vote!")
except TypeError:
    print("Error occured")
    