# Modules
import Demo

lst = [1, 5, 7, 9, 11, 13]
print(Demo.sum(lst))
print(Demo.mult(lst))


def dif(a, b):
    return a - b


print(dif(4, 2))
print(dif(2, 4))


def dec_dif(function):
    def change(a, b):
        if b > a:
            a, b = b, a
        return function(a, b)
    return change


dif = dec_dif(dif(2, 4))
print(dif(2, 4))
