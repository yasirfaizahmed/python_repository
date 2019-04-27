import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')
import random
x_cor = []
y_cor = []
for i in range(10):
    x_cor.append(random.randint(0, 9))
    y_cor.append(random.randint(0, 10))
print("x_cor :", x_cor)
print("y_cor :", y_cor)

sum_x = 0
for i in x_cor:
    sum_x = sum_x+int(i)
mean_x = sum_x/len(x_cor)

sum_y = 0
for i in y_cor:
    sum_y = sum_y+int(i)
mean_y = sum_y/len(y_cor)

print("mean_x :", mean_x)
print("mean_y :", mean_y)

sd_x = 0
x = []
for i in range(4):
    x.append(random.randint(0,5))
print("x_samples :", x)
for i in x:
    j = int(i)
    sd_x = sd_x+(j - mean_x)**2
sd_x = sd_x**0.5
sd_x = sd_x/(len(x)-1)
print("sd_x :",sd_x)

sd_y = 0
y = []
for i in range(4):
    y.append(random.randint(0,5))
print("y_samples :", y)
for i in y:
    j = int(i)
    sd_y = sd_x+(j - mean_y)**2
sd_y = sd_y**0.5
sd_y = sd_y/(len(y)-1)
print("sd_y :",sd_y)

#plt.scatter(x_cor,zeros,color='r')
plt.scatter(x_cor,y_cor,color='g')
plt.scatter(mean_x,0,color='r')
plt.scatter(0,mean_y,color='b')
plt.show()

def co_effecient_correlation():
    global x_cor, mean_x
    global y_cor, mean_y
    nr0 = 0
    for i in x_cor:
        i = int(i)
        nr0 = nr0 + (i - mean_x)
    nr1 = 0
    for i in y_cor:
        i = int(i)
        nr1 = nr1 + (i - mean_y)
    nr = nr0*nr1

    dr0 = 0
    for i in x_cor:
        i = int(i)
        dr0 = dr0 + (i - mean_x)**2
    dr1 = 0
    for i in y_cor:
        i = int(i)
        dr1 = dr1 + (i - mean_y)**2
    dr = (dr0*dr1)**0.5
    r = nr/dr
    print(r)
co_effecient_correlation()