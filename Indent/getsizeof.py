from sys import getsizeof
from numpy import full

var = "hello"
arr = full((5, 5), ' ', dtype=str)
lst = arr.tolist()
print(getsizeof(var))
print(getsizeof(arr))
print(getsizeof(lst))
print(lst)
print(arr)
