## List in Python
- https://www.google.com/search?q=membership+operator+in+python&rlz=1C1RXQR_enIN1100IN1100&oq=membership+ope&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDM2MjBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


>let's delve into lists in Python. Lists are one of the most versatile and commonly used data structures in Python. They are mutable, ordered collections of items, allowing you to store and manipulate a sequence of elements.



## List Methods:
- append(): Adds an element to the end of the list.
- extend(): Appends elements from another list to the end.
- insert(): Inserts an element at a specified position.
- remove(): Removes the first occurrence of a value.
- pop(): Removes and returns the element at a specified index.
- index(): Returns the index of the first occurrence of a value.
- count(): Returns the number of occurrences of a value.
- sort(): Sorts the list in ascending order.
- reverse(): Reverses the elements of the list in place.


## List Comprehension:

```python
    squares = [x**2 for x in range(1, 6)]
    print(squares)  # Output: [1, 4, 9, 16, 25]
```

## List Operations:

- You can perform various operations on lists, such as concatenation (+) and repetition (*).

```python
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    concatenated_list = list1 + list2
    repeated_list = list1 * 3
```
