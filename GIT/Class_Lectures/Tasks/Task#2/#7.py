str = input("Enter a string: ")
for i in str:
    if i.lower() not in "aeiou":
        print(i, end="")
