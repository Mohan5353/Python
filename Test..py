import pandas as pd
import numpy as np

data = pd.read_excel("StudentData.xlsx", usecols="A")
data = pd.Series(data["Id.No"]).tolist()
i = 0
count = 0
for Id in range(1, 1159):
    if data[i] != "N20" + ("0" * (4 - len(str(Id)))) + str(Id) and data[i] != data[4]:
        # pass
        count += 1
        print(Id)
    else:
        # print(i)
        i += 1
    # print(data[Id])
print(count)
