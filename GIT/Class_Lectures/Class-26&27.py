# Polymorphism->Overloading,Ducktyping,Overriding,Overloading
#
#
#
# Ducktyping
class maa:
    def present(self):
        print("RRR")


class etv:
    def present(self):
        print("Temper")


class Television:
    def display(self, movie):
        movie.present()


m = maa()
e = etv()
t = Television()
t.display(m)
t.display(e)


# Operator Overloading
class complex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __add__(self, other):
        return complex(self.real + other.real, self.imaginary + other.imaginary)

    def __sub__(self, other):
        return complex(self.real - other.real, self.imaginary - other.imaginary)

    def disp(self):
        print(f"{self.real} + {self.imaginary}i")


c1 = complex(1, 2)
c2 = complex(3, 4)
c3 = c1 + c2
c3.disp()
c3 = c1 - c2
c3.disp()


# Method overloading
class number:
    def sum(self, a=0, b=0, c=0):
        if a is 0 and b is 0 and c is 0:
            return 0
        elif b is 0 and c is 0:
            return a
        elif c is 0:
            return a + b
        else:
            return a + b + c


n = number()
print(n.sum(1, 2, 3))

# Method Overriding


class A:
    def display(self):
        print("A")


class B(A):
    def display(self):
        print("B")


a = A()
b = B()
a.display()
b.display()
