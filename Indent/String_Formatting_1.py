text = "Hello World"
print(f"{text = }")


class A:
    def __str__(self):
        return '__str__'

    def __repr__(self):
        return object.__repr__(self)


a = A()
print(f"{a = }")
