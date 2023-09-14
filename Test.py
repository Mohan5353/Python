from numpy import full

arr = full((5, 5), ' ', dtype=str)


def fun1():
    print('\n' * 3)
    for i in range(5):
        print(" " * 44, "| {} | {} | {} | {} | {} |".format(arr[i][0], arr[i][1], arr[i][2], arr[i][3], arr[i][4]))
    print("1   2   3   4   5".rjust(64))
    return None


def fun2():
    print('\n' * 3)
    for i in range(5):
        print(" " * 44, "|", end=" ")
        for j in range(5):
            print(arr[j][i], end=" | ")
        print('\n')
    return None

fun2()