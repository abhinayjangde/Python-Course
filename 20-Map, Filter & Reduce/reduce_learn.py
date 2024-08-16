from functools import reduce
# nums = [55]
nums = [i for i in range(1,11)]
# print(nums)

sum = reduce(lambda x,y: x+y, nums)
print(sum)