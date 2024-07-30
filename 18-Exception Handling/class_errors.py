class AgeError(Exception):
    pass
class DobError(Exception):
    pass 

try:
    age = int(input("Enter your age: "))
    if(age<18):
        raise AgeError("You cannot vote")
except AgeError as e:
    print("error: ",e)
else:
    print("You can vote")