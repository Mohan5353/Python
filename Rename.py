from os import listdir, renames

path = r"G:\Wednesday"
for i, j in enumerate(listdir(path)):
    renames(path + "\\" + j, path + "\\Episode_" + str(i + 1) + ".mp4")
