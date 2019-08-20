import random
import matplotlib.pyplot as plt

x_data = []    #independent variable x in data give
y_data = []    #dependent variable y in data give
for i in range(0,10,1):    #creating a dataset of 100 values each
    x_data.append(random.randint(1, 20))    #random no. from 1 to 20
    y_data.append(random.randint(1, 20))    #----||-----||-----||---
    plt.plot(x_data[i], y_data[i],'ro')    #plotting the random data with red dots
#x_data = [4,8,6,5,9,7,12,3,5]
#y_data = [4,5,1,6,8,2,10,4,6]
y_pri = []    #list for predicted var

J_arr = []
def best_m():
    m = 0.01    #slope starts from m = 0.01
    while(m <= 50):
        y_pri.clear()    #clearing the array
        for i in range(len(x_data)):
            y_pri.append(m*x_data[i])    #y = mx plus c , here c is not included

        J = 0
        for i in range(len(x_data)):    #the cost function is calculated
            J += ((y_pri[i] - y_data[i])**2)/(2*10)
        J_arr.append(J)    #the function value is appended to array
        m += 0.1
    print(J_arr)

plt.plot(x_data, y_data, 'ro')    #plotting the random data
plt.show()
best_m()    #calling the function

m_arr_test = []
m_test = 0.1
while(m_test <= 50):
    m_arr_test.append(m_test)
    m_test += 0.01
plt.plot(m_arr_test, J_arr, 'ro')
plt.show()


