
age = int(input("Enter your age: "))
if(age<18):
    raise ValueError("You are not eligible for vote")
else:
    print("You can vote")
