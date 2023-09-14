import time

import pandas as pd
from PIL import Image

data = pd.read_excel(
    r"D:\Academics\IT\Python\P1-S1 and E1S1(2019&2018-Batch) EST EXAM SHUFFLE AS ON "
    r"22-10-2021 FOR DISPLAY .xlsx", usecols=["Id.No", "Password"])
file = dict(zip(data.loc[:, 'Id.No'], data.loc[:, 'Password']))

while True:
    Id = input("Enter Id or Quit :")
    if Id == 'Quit':
        break
    Id = Id.upper()
    try:
        print(file[Id])
        if input('Show Image?(Y/n) ').lower() == 'y':
            try:
                Image.open(r'G:/Pics_SMS/' + Id + r'.jpg').show()
            except Exception as e:
                print("\nFile Not Located...!", "\nException Raised:", e, end='\n\n')
    except Exception as e:
        print("Incorrect ID......", "Exception Raised:", e)
print("Program Closed....!")
time.sleep(0.5)
