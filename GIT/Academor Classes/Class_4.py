from time import sleep

lst1 = [10, 20, 30, 40, 50, 60, 70, 80, 90]
lst2 = [100, 200, 300, 400, 500]
print(lst1[2:5])
print(lst1[:5])
print(lst1[2:])
print(lst1[:])
print(lst1 + lst2)
string1 = "Hello World"
string2 = "Hello"
string3 = "Hello World"
print(string1 == string2)
print(string2 + string3)
for i in range(10):
    print(('*' * (2 * i + 1)).center(2 * 10))
sleep(10)
