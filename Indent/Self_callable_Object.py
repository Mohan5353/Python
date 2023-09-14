class Car:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def __call__(self):
        return f"Brand: {self.brand} Price: {self.price}"


c1 = Car("BMW", 1000)
print(c1())
