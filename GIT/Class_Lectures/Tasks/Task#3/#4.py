# Break, Continue, Pass are the loop control statements

# Break is used to exit the loop
for i in range(10):
    if i == 5:
        break
    print(i)

# Continue is used to skip the current iteration and continue with the next iteration
for i in range(10):
    if i == 5:
        continue
    print(i)

# Pass is used to do nothing just to skip statements in the loop
for i in range(10):
    pass
