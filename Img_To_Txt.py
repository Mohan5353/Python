from PIL import Image
from pytesseract import pytesseract
import os

path_to_tess = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
path_to_imgs = r"C:\Users\MohanKumar\Pictures\Screenshots"
pytesseract.tesseract_cmd = path_to_tess
for root, dirs, file_names in os.walk(path_to_imgs):
    for file_name in file_names:
        if file_name != "desktop.ini":
            img = Image.open(path_to_imgs + r"\\" + file_name)
            text = pytesseract.image_to_string(img)
            print(text, end="-" * 100)
            print()
