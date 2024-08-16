
## 1. Walrus Operator (:=)
Introduced in Python 3.8, the walrus operator allows assignment expressions, enabling assignment and return of a value in a single expression. This is particularly useful in loops and comprehensions.
```python
# Not Allowed
print(is_alive=False)
# Allowed
print(is_active:=True)
```

## 2. Matrix Multiplication Operator (@)
Introduced in Python 3.5, the '@' operator is used for matrix multiplication, which is especially useful in numerical computing and machine learning applications.
```python
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

# Matrix multiplication
c = a @ b
print(c)
```

## 3. New String Formatting (f-strings)
Introduced in Python 3.6, f-strings provide a way to embed expressions inside string literals, using curly braces '{}'.
```python
name = "Abhinay"
age = 21
print(f"My name is {name} and I am {age} years old.")
```
## 4. Enhanced Unpacking
Python 3.5 introduced extended unpacking with the '*' operator to allow more flexible unpacking operations.
```python
a, *b, c = [1, 2, 3, 4, 5]
print(a)  # 1
print(b)  # [2, 3, 4]
print(c)  # 5
```
## 5. Positional-Only Parameters
Introduced in Python 3.8, positional-only parameters are defined by adding a '/' in the function signature. These parameters can only be passed positionally, not as keyword arguments.
```python
def greet(name, /, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet("Abhinay"))  # Works
# print(greet(name="Abhinay"))  # Raises TypeError
```

## 6. Keyword-Only Parameters
Defined by adding '*' in the function signature, parameters following '*' can only be passed as keyword arguments.
```python
def greet(*, name, greeting="Hello"):
    return f"{greeting}, {name}!"

print(greet(name="Abhinay"))  # Works
# print(greet("Abhinay"))  # Raises TypeError
```
These new operators and enhancements make Python more expressive and capable of handling various programming paradigms more efficiently.
