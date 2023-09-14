class television:
    shape = "Rectangle"

    def __init__(self, brand, size):
        self.brand = brand
        self.size = size

    def display(self):
        print(self.shape, self.brand, self.size)

    class channel:
        def __init__(self, brand, size, channel_name):
            self.channel_name = channel_name
            self.brand = brand
            self.size = size

        def display(self):
            print(self.channel_name, self.brand, self.size)


t1 = television("Samsung", 32)
t1.display()
t2 = television("Sony", 64)
t2.display()
print(t1.shape)
print(t2.shape)
print(television.shape)
t3 = television.channel("Sony", 64, "Sony Channel")
t3.display()
