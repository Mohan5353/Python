import abc

tup = (1, 2, 3)
it = iter(tup)
print(next(it))
print(next(it))
print(next(it))


def my_gen(n: int):
    value = 0
    while value < n:
        yield value
        value += 1


for i in my_gen(5):
    print(i)
