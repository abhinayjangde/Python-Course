
try:
    age = int(input("Enter your age: "))
except ValueError as e:
    print(e)
    print("Only numbers are allowed")
else:
    print(f"Your age is {age}")
