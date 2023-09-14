class car:
    def __init__(self, brand):
        self.brand = brand

    def __str__(self):
        return f"{self.brand}"

    def __repr__(self):
        return object.__repr__(self)


c1 = car("BMW")
print(f"{c1}")
