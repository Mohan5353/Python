from cryptography.fernet import Fernet

with open("Hack.txt", "rb") as fp:
    key = fp.read()
fernet = Fernet(key)
with open('E:\\H\\18835.csv', 'rb') as fp:
    print(fp.read())
