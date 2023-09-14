from os import listdir, renames

if "test.xyzmail" == input():
    path = r"E:\Records"
    for i in listdir(path):
        renames(path + "\\" + i, path + "\\" + i[:-3] + "mp4")
