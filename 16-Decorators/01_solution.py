def uppercase_decorator(fx):
    def wrapper(*args,**kwargs):
        return fx(*args,**kwargs).upper()
    return wrapper
    
@uppercase_decorator  
def greet(name):
    return f"Hello, {name}"

print(greet("Preeti"))