# arr = [1,4,2,6,12,10]
# result = list(filter(lambda n : n > 4, arr))
# print(result)
nums = [i for i in range(1,11)]
even = list(filter(lambda n: n%2==0, nums))
print(even)