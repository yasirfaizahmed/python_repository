#reference links
#http://polynomialregression.drque.net/math.html
#https://neutrium.net/mathematics/least-squares-fitting-of-a-polynomial/#:~:text=The%20general%20polynomial%20regression%20model%20can%20be%20developed%20using%20the,expected%20values%20from%20the%20dataset.
#https://dhirajkumarblog.medium.com/linear-regression-without-sklearn-from-scratch-5c83b46642f8


########################          USING CRAMERS RULE #############

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

def predict_values(degree, coeff, max):     #returns max * 10 predicted values as an array
    predict = []
    eqn = 0
    inc = 0
    for i in range(0, max*10):  # creating the predicted target y's from the formed model, min term in sample to max term in sample*10
        inc += 0.1
        for j in range(degree):
            eqn += coeff[degree - j - 1] * (inc) ** (degree - j - 1)
        predict.append(eqn)
        eqn = 0
    return predict


df = pd.read_csv("sample.csv")
np_df = df[['x','y']].to_numpy()
x = np_df[0:, 0]
y = np_df[0:, 1]

degree = 5     #max degree for the model
for q in range(degree):
    coeff = poly_reg(y, x, q)
    print(coeff)

    predict = predict_values(degree=q, coeff=coeff, max=20)

    plt.plot(np.arange(0, 20, 0.1), predict)
    plt.scatter(x, y, color='red', marker='+')

    plt.text(5, 460, "Degree = ")
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(q)
    plt.pause(1.0)
    plt.clf()

plt.show()
