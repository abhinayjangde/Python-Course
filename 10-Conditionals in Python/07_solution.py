side1=3
side2=3
side3=3

if side1==side2==side3:
    print("equilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("isosceles")
else:
    print("scalene")