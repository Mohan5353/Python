import time

# a = int(input("Enter 1st Number :"))
# try:
#     b = int(input("Enter 2nd Number :"))
#     print("Running code.....")
#     print(float(a) / b)
# except Exception as e:
#     print("Exception Raised : " + str(e))
#     exit(1)
# finally:
#     print("Program Ended.....")


# with open("File.txt", "w+") as fp:
#     fp.write("Hello")
#     fp.flush()
#     fp.write(" Hi")
# with open("File.txt", "r") as fp:
#     r = fp.read()
#     print(r)


l = [1, 2, 5, 3, 7, 4, 0, 6]
a = int(input("Enter a Number : "))
# for i in l:
#     if l[i] == a:
#         print("value Found at position", i)
#         break


# l.sort()  # [0,1,2,3,4,5,6,7]
# mid = (len(l) - 1) // 2


# if a == l[mid]:
#     print("Number found_1")
# elif a > l[mid]:
#     for i in range(mid + 1, len(l)):
#         if a == l[i]:
#             print("Number found_2")
# else:
#     for i in range(mid - 1, -1, -1):
#         if a == l[i]:
#             print("Number found_3")


# for i in range(0, len(l)):
#     if a == l[i]:
#         print("Number Found_1", i)
#         break
#     elif a > l[i]:
#         i = (len(l) - 1) // 2


# for i in range(len(l)):
#     for j in range(i + 1, len(l)):
#         if l[i] > l[j]:
#             print("Swaped", l[i], l[j])
#             l[i], l[j] = l[j], l[i]
# print(l)


# for i in range(len(l) - 1, 0, -1):
#     for j in range(i):
#         if l[j] > l[j + 1]:
#             l[j], l[j + 1] = l[j + 1], l[j]
# print(l)


for i in range(len(l) - 1):
    small = i
    for j in range(i + 1, len(l)):
        if l[small] > l[j]:
            small = j
    l[i], l[small] = l[small], l[i]

print(l)
