# def cube(n):
#     return n*n*n
# print(cube(3))

arr = [1,4,2,6,12,10]
# newList = []
# for i in arr:
#     newList.append(cube(i))
# print(newList)
new = list(map(lambda x: x*x*x,arr))
print(new)