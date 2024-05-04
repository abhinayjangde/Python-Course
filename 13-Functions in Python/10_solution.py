def even_numbers(limit):
    for i in range(2,limit+1,2):
        yield i

for n in (even_numbers(10)):
    print(n)