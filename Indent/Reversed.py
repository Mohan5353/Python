from sys import getsizeof as size
from typing import Any


def display(var: Any) -> None:
    print(f"{var}: {size(var)} Bytes")


my_list = ["A1", "A2", "A3"]
my_str = "Python is fun!"
display(my_list)
display(my_str)
rev_list = reversed(my_list)
rev_str = reversed(my_str)
display(rev_list)
display(rev_str)
display("".join(rev_str))

print(next(rev_list))
print(next(rev_list))
display(list(rev_list))
