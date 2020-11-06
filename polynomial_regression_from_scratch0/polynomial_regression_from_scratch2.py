#reference links
#http://polynomialregression.drque.net/math.html
#https://neutrium.net/mathematics/least-squares-fitting-of-a-polynomial/#:~:text=The%20general%20polynomial%20regression%20model%20can%20be%20developed%20using%20the,expected%20values%20from%20the%20dataset.
#https://dhirajkumarblog.medium.com/linear-regression-without-sklearn-from-scratch-5c83b46642f8


################            USING CRAMERS RULE ############

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np

def poly_reg(y, x, degree):
    M = np.zeros(shape=(degree, degree))
    rhs = np.zeros(shape=(degree,1))

    for i in range(degree):
        for j in range(degree):
            M[i][j] = sum(x**(i+j))
    for i in range(degree):
        rhs[i] = sum(y*(x**i))

    det_M = np.linalg.det(M)
    det = []
    temp = np.zeros((degree, degree))
    temp[:,:]= M[:,:]
    for i in range(degree):
        M[:, i] = rhs[:,0]
        det.append(np.linalg.det(M))
        M[:,:] = temp[:,:]
    det = det/det_M
    return det


def predict_array(degree, coeff, length):     #returns max * 10 predicted values as an array
    predicted = []
    eqn = 0
    inc = 0
    for i in range(0, length):  # creating the predicted target y's from the formed model, min term in sample to max term in sample*10
        inc += 0.1
        for j in range(degree):
            eqn += coeff[degree - j -1] * (inc) ** (degree - j -1)
        predicted.append(eqn)
        eqn = 0
    return predicted

def predict_target(x_value, degree, coeff):
    eqn = 0
    for j in range(degree):
        eqn += coeff[degree - j - 1] * (x_value) ** (degree - j - 1)
    return eqn


def R_squared(x, y, degree, coeff):         ##ineffective R square for non linear regressions!!!!!!R SQUARE CANNOT BE APPLIED TO NON LINEAR REGRESSIONS!!!!!!!!!
    mean_y = sum(y) / len(y)
    predicted = []
    for i in range(len(y)):
        predicted.append(predict_target(x[i], degree-1, coeff))
    R_square = sum((y - predicted) ** 2) / sum((y - mean_y) ** 2)
    return R_square


df = pd.read_csv("sample.csv")
np_df = df[['x','y']].to_numpy()
x = np_df[0:, 0]
y = np_df[0:, 1]

degree = 13     #max degree for the model
coeff = []
for q in range(degree):
    coeff = poly_reg(y, x, q)
    #print(coeff)

    predicted = predict_array(degree=q, coeff=coeff, length=200)


    plt.plot(np.arange(0, 20, 0.1), predicted)
    plt.scatter(x, y, color='red', marker='+')

    plt.text(5, 460, "Degree = ")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(q)
    plt.pause(0.1)
    plt.clf()





