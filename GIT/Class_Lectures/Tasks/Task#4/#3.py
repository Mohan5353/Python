x = input("Enter a List of Meals Served Separated by Commas: ").split(",")
flag = 0
for i in range(len(x) - 1):
    if x[i] == x[i + 1]:
        flag = 1
        break
if flag == 1:
    print("Yes")
else:
    print("No")
