import matplotlib.pyplot as plt
import numpy as np
#import random

y0 = [4,5,1,6,8,2,10,4,6]
x0 = [4,8,6,5,9,7,12,3,5]
'''lem = input("Enter no. of co_ordinates: ")
len_i = int(lem)'''
len_i = len(x0)
'''for i in range(len_i):
    x = random.randint(0, 100)
    x0.append(x)
    y = random.randint(0, 100)
    y0.append(y)
print("x0 =", x0)
print("y0 =", y0)'''

sum_x = 0
sum_y = 0
for i in range(len_i):
    sum_x = x0[i]+sum_x
    sum_y = y0[i]+sum_y
print(sum_x, sum_y)

mean_x = sum_x/len_i
mean_y = sum_y/len_i

xb = []
yb = []

for i in range(len_i):
    xb.append(x0[i] - mean_x)
    yb.append(y0[i] - mean_y)
print(xb , yb)

junk = []
for i in range(len_i):
    junk.append(xb[i]*yb[i])
junk_nr = 0
for i in range(len_i):
    junk_nr = junk[i] + junk_nr

flag = []
for i in range(len_i):
    flag.append((xb[i])*(xb[i]))
dr = 0
for i in range(len_i):
    dr = dr + flag[i]

slope = junk_nr/dr
print(slope)

plt.plot(x0, y0, 'ro')
flag = np.linspace(0, 10, 100)
plt.plot(flag, slope*flag, label = 'linear')
plt.show()
plt.show()
