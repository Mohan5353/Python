import os

with open("Sample_File.txt", 'w') as fp:
    max = 1024 * 1024
    while os.path.getsize("Sample_File.txt") < max:
        fp.write('a')
