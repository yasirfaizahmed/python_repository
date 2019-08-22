import random
import matplotlib.pyplot as plt

x_data = []    #independent variable x in data give
y_data = []    #dependent variable y in data give
for i in range(0,10,1):    #creating a dataset of 100 values each
    x_data.append(random.randint(1, 20))    #random no. from 1 to 20
    y_data.append(random.randint(1, 20))    #----||-----||-----||---
#x_data = [4,8,6,5,9,7,12,3,5]
#y_data = [4,5,1,6,8,2,10,4,6]
y_pri = []    #list for predicted y

J_arr = []
perfect_J = 100    #dummy value
m_initial = 0    #initial value of slope m
m_increment = 0.01   #resolution of slope m
m_max = 10    #max value of slope m
def best_m():    #only for one linear, c= 0  variable, with max_m = 50
    m = m_initial    #slope starts from m = 0.01
    while(m <= m_max):
        y_pri.clear()    #clearing the array
        for i in range(len(x_data)):
            y_pri.append(m*x_data[i])    #y = mx plus c , here c is not included

        J = 0
        for i in range(len(x_data)):    #the cost function is calculated
            J += ((y_pri[i] - y_data[i])**2)/(2*10)
        J_arr.append(J)    #the function value is appended to array
        m += m_increment    #incriment in slope

plt.plot(x_data, y_data, 'ro')    #plotting the random data
plt.show()
best_m()    #calling the function
print(perfect_J)
#print(J_arr)

m_arr_test = []    #for plotting the J values and taking the best J
m_test = 0
i = 0
while(m_test <= m_max):
    m_arr_test.append(m_test)
    m_test += m_increment
    if (J_arr[i] < perfect_J):
        perfect_J = J_arr[i]
    i += 1

haha = 0
for i in range(len(J_arr)):    #to get the best slope m
    if(J_arr[i] == perfect_J):
        haha = i
best_slope = haha*m_increment

print("lowest J: ",perfect_J)
print("best slope found at: ",haha)
print("BEST SLOPE: ",best_slope)
plt.plot(m_arr_test, J_arr)
plt.show()
