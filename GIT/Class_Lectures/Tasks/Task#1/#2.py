# Count is used to count a specific element in a list
def count(lst, element):
    c = 0
    for i in lst:
        if i == element:
            c += 1
    return c


data = [23, 45, "Pavan", 78.5, 90, 200, 130.5, "Pavan", 78.5]
print(count(data, "Pavan"))
