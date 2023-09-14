# Class Methods
# Instance Methods
class television:
    shape = "Rectangle"

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    # Modifier
    def change(self):
        self.brand = "Sony"

    # Accessor
    def display(self):
        print(self.shape, self.brand, self.size)

    # Class Method
    @classmethod
    def channel(cls):
        cls.shape = "Square"

    # Static Method
    @staticmethod
    def info():
        print("This is static method")


t1 = television("Samsung", 32)
t1.display()
t2 = television("Sony", 64)
t2.display()
print(t1.shape)
print(t2.shape)
t1.change()
t1.info()
television.info()
television.channel()
print(television.shape)
television.shape = "Round"
print(television.shape)
t1.channel()
print(television.shape)
t1.display()
print("\n\n\n")


# Single Level Inheritance
class A:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)


class B(A):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(self.name)


a = A("A")
b = B("B")
a.display()
b.display()


# Multi Level Inheritance
class A:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name, "In Class A")


class B(A):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(self.name, "IN Class B")


class C(B):
    def __init__(self, name):
        super().__init__(name)

    def display(self):
        print(self.name, "In Class C")


a = A("A")
b = B("B")
c = C("C")
a.display()
b.display()
c.display()


# Multiple Inheritance
class A:
    name = "A"

    @classmethod
    def funA(cls):
        print(cls.name)


class B:
    name = "B"

    @classmethod
    def funB(cls):
        print(cls.name)


class C(A, B):
    name = "C"

    @classmethod
    def funC(cls):
        print(cls.name)


c = C()
c.funA()
C.funB()
C.funC()
