import pandas as pd

file = r"StudentData.xlsx"
df = pd.read_excel(file)
print(df.info())
# print(df)
