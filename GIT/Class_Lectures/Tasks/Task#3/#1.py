a = 10
b = 20

# 1st Way
a, b = b, a

# 2nd Way
a = a + b
b = a - b
a = a - b

# 3rd Way
temp = a
a = b
b = temp

# 4th Way
a = a ^ b
b = a ^ b
a = a ^ b
