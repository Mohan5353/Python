import functools as ft


def sum(lst):
    print(__name__)
    return ft.reduce(lambda a, b: a + b, lst)


def mult(lst):
    return ft.reduce(lambda a, b: a * b, lst)


if __name__ == "__main__":
    lst = [1, 5, 7, 9, 11, 13]
    print(sum(lst))
    print(mult(lst))
