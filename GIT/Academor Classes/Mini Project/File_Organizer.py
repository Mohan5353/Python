import os
import shutil
from customtkinter import filedialog


class File_organizer:
    def __init__(self):
        path = filedialog.askdirectory(title="Select Folder")
        list_of_files = os.listdir(path)
        for files in list_of_files:
            name, extension = os.path.splitext(files)
            extension = extension[1:]
            if not os.path.exists(path + '/' + extension):
                os.makedirs(path + '/' + extension)
            shutil.move(path + '/' + files, path + '/' + extension + '/' + files)

# File_organizer()
