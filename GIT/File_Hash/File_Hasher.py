import hashlib

hsh = hashlib.sha256()
with open(r"D:\Academics\IT\Python\Book\python_Book.pdf", 'rb') as fp:
    while True:
        chunk = fp.read(1024*1024)
        if not chunk:
            break
        hsh.update(chunk)

print(hsh.hexdigest())
