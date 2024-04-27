# 4! = 4x3x2x1
# 5! = 5x4x3x2x1
# 0! = 1
# 1! = 1
n = 6
factorial=1
for i in range(1,n+1):
    factorial = factorial * i
print(f"The factorial of {n} is {factorial} ")