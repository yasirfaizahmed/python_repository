import hashlib
import time
start = time.time()
pas = input("\nplease enter the md5 hash:")
pw_file = input("\nenter the file location:")
count = 0
try:
    pw_file = open(pw_file,mode='r')
except:
    print("\nfile not found")
    quit()
for password in pw_file:
    sdf = password.strip()
    encoded = sdf.encode('utf-8')
    hashed = hashlib.md5(encoded)
    lol = hashed.hexdigest()
    print("trying with:",lol)
    count +=1
    if pas==lol:
        print("password matched!\npassword is:",password)
        print("at:",count)
        break
else :
    print("passwords did not matched")
end = time.time()
timee = end - start
print("time took:",timee)
