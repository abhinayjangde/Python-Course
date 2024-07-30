
try:
    age = int(input("Enter your age: "))
except ValueError as e:
    # print(e)
    print("Only numbers are allowed")
except KeyboardInterrupt:
    print("Keyborad Interrupt")
except Exception:
    print("Error")
else:
    print(f"Your age is {age}")
finally:
    print("Allways runs")