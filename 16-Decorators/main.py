
def greet(fx):
    def wrapper(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("Bye")
    return wrapper

@greet
def name():
    print("Abhi")

@greet
def user(username):
    print(f"{username}")

# result = greet(name)
# result()
# name()
user("ANkit")