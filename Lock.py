from os import listdir, renames

path = r"E:\Records"
for i in listdir(path):
    renames(path + "\\" + i, path + "\\" + i[:-3] + "csv")
