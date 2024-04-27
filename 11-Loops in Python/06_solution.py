fibo_series=[0,1]
n = 5
for i in range(2,n+1):
    next_term = fibo_series[-1] + fibo_series[-2]
    fibo_series.append(next_term)

print(fibo_series)