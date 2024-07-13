
def repeat(n):
    def decorator(fx):
        def wrapper(*args,**kwargs):
            for _ in range(n):
                fx(*args,**kwargs)
        return wrapper
    return decorator

@repeat(4)
def name():
    print("Hello Abhi!")

name()