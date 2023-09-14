import time
from math import *
from numpy import array

Addition = lambda a, b: a + b
Subtraction = lambda a, b: a - b
Absolute = lambda a, b: abs(a)
Multiplication = lambda a, b: a * b
Division = lambda a, b: a / b
Remainder = lambda a, b: a % b
Power = lambda a, b: pow(a, b)
Sin = lambda a, b: sin(radians(a))
Cos = lambda a, b: cos(radians(a))
Tan = lambda a, b: tan(radians(a))
Inverse = lambda a, b: 1 / a
_ = 0
if __name__ == "__main__":
    # while True:
    # print("1.Add".ljust(15), "2.Sub".ljust(15), "3.Absolute".ljust(15))
    # print("4.Multiply".ljust(15), "5.Divide".ljust(15), "6.Remainder".ljust(15))
    ops = array(["Addition", "Subtraction", "Absolute", "Multiplication", "Division", "Remainder", "Sin", "Cos",
                 "Tan", "Power", "Inverse", "Exit"], dtype=str)
    while True:
        i1, i2 = 0, 0.0
        for it, i in enumerate(ops):
            if it % 3 == 0:
                print('\n')
            print((f"{it + 1}." + i).ljust(20), end='')
        try:
            op = int(input("\n\nEnter Operation: "))
            if op > 12 or op < 1:
                raise Exception("OverFlow Error")
            elif op == 12:
                break
            i1 = int(eval(input("Enter No. 1: ")))
            if op in [1, 2, 4, 5, 6, 7]:
                i2 = int(eval(input("Enter No. 2: ")))
            _ = eval(ops[op - 1] + f"({i1},{i2})")
            print('\nAnswer=', _)
        except Exception as e:
            print(e)
        time.sleep(2.33)

    print("_Calculator Closed_".center(60, "*"))
    time.sleep(1.33)
