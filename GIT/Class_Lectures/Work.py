# Take Class using init method in inheritance
# Code Magical Methods Product of marks of 3 student to create 4th student
# class market 2 prices for two products, use __sub__ to create 3rd product
# class Student def Work subject.homework(),science(read method),maths(Practice method)
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def disp(self):
        print(self.name, self.age)


class B:
    def __init__(self, name, age):
        self.name1 = name
        self.age1 = age

    def disp(self):
        print(self.name1, self.age1)


class C(A):
    def __init__(self, name, age):
        super().__init__(name, age)


class D(A, B):
    def __init__(self, name, age, name1, age1):
        super().__init__(name, age)
        B.__init__(self, name1, age1)

    def disp(self):
        A.disp(self)
        B.disp(self)


d = D("Ram", 20, "Rahul", 20)
d.disp()


class student:
    def __init__(self, m):
        self.m = m

    def disp(self):
        print(self.m)

    def __add__(self, *other):
        sum = self.m
        for i in other:
            sum += i.m
        return sum


s1 = student(10)
s2 = student(20)
print(s1 + s2)


class market:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def disp(self):
        print(self.p1, self.p2)

    def __sub__(self, other):
        res = market(self.p1 - other.p1, self.p2 - other.p2)
        return res


m1 = market(10, 20)
m2 = market(20, 30)
m3 = m1 - m2
m3.disp()


class science:
    @staticmethod
    def homework():
        print("Read Chapter 3")


class maths:
    @staticmethod
    def homework():
        print("Practice Chapter 3")


class student1:
    def work(self, subject):
        subject.homework()


stu = student1()
stu.work(science)
stu.work(maths)
