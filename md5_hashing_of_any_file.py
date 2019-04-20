import hashlib
password = input("\nenter  a password to be hashed:")
sdf = password.strip()
encoded = sdf.encode('utf-8')
print(encoded)
hashed = hashlib.md5(encoded)
print(hashed)
lol = hashed.hexdigest()
print(lol)
