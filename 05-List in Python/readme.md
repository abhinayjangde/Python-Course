## List in Python
- https://www.google.com/search?q=membership+operator+in+python&rlz=1C1RXQR_enIN1100IN1100&oq=membership+ope&gs_lcrp=EgZjaHJvbWUqBwgAEAAYgAQyBwgAEAAYgAQyBggBEEUYOTIHCAIQABiABDIHCAMQABiABDIHCAQQABiABDIHCAUQABiABDIHCAYQABiABDIHCAcQABiABDIHCAgQABiABDIHCAkQABiABNIBCDM2MjBqMGo3qAIAsAIA&sourceid=chrome&ie=UTF-8


>let's delve into lists in Python. Lists are one of the most versatile and commonly used data structures in Python. They are mutable, ordered collections of items, allowing you to store and manipulate a sequence of elements.



## List Methods:
| Method   | Description                                                        |
|----------|--------------------------------------------------------------------|
| append() | Adds an element at the end of the list                             |
| clear()  | Removes all the elements from the list                             |
| copy()   | Returns a copy of the list                                         |
| count()  | Returns the number of elements with the specified value            |
| extend() | Add the elements of a list (or any iterable), to the end of the current list |
| index()  | Returns the index of the first element with the specified value    |
| insert() | Adds an element at the specified position                          |
| pop()    | Removes the element at the specified position                      |
| remove() | Removes the first item with the specified value                    |
| reverse()| Reverses the order of the list                                     |
| sort()   | Sorts the list                                                     |



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
