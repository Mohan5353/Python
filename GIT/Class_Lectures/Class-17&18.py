import functools as ft

x = lambda a, b: a + b
print(x(1, 2))
lst = [1, 2, 3, 4, 5]
age = [36, 18, 19, 21, 33]
print(list(map(lambda x: x * 2, lst)))
print(list(filter(lambda x: x > 17, age)))
lst = [1, 2, 3, 4, 5]
print(ft.reduce(lambda a, b: a + b, [1, 2, 3, 4, 5]))
