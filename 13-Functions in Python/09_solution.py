def print_kwargs(**kwargs):
    # print(type(kwargs))
    for key,value in kwargs.items():
        print(f"{key} : {value} ")
print_kwargs(age=22,name="abhi",roll="Coder")
