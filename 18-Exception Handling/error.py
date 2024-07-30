try:
    a = int(input("Enter a number: "))
    b = int(input("Enter a second number: "))
    print(a/b)
except ZeroDivisionError:
    print("division by zero")
except ValueError:
    print("Only number are acceptable.")


print("Rest of code")