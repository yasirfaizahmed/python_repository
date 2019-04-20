import time
start = time.time()
my_file = input("enter the file path here:")
try:
    my_file = open(my_file, mode='r')
except:
    print("\nfile not found")
    quit()
num = 0
for lines in my_file:
    words = lines.strip()
    print(words)
    num +=1
print(num)
end = time.time()
timee = (start - end)*-1
print(timee)