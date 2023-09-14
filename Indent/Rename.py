from os import listdir, renames

path = r"E:\Records"
for i, j in enumerate(listdir(path)):
    renames(path + "\\" + j, path + "\\" + str(i + 1) + ".mp4")
