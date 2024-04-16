import sys

# Create an object
my_object = [1, 2, 3]
# my_object = 90
another = my_object
me_another = my_object

# Get the reference count
count = sys.getrefcount(my_object)

# Subtract 1 from the count to get the actual number of references
actual_count = count - 1

print("Number of references to my_object:", actual_count)
