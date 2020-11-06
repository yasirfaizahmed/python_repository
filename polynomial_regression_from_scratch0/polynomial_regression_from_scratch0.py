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


df = pd.read_csv("sample.csv")
np_df = df[['x','y']].to_numpy()
x = np_df[0:, 0]
y = np_df[0:, 1]

for q in range(13):
    degree = q
    coeff = poly_reg(y, x, degree)
    print(coeff)

    predict = []
    eqn = 0
    for i in range(-2,20):
        for j in range(degree):
            eqn += coeff[degree-j-1]*(i)**(degree-j-1)
        predict.append(eqn)
        eqn = 0

    plt.plot(range(-2,20), predict)
    plt.scatter(x, y, color='red', marker='+')

    plt.text(5, 460, "Degree = ")
    plt.xlabel("X_independent var.")
    plt.ylabel("Y_dependent var.")
    plt.title(q)
    plt.pause(1.0)
    plt.clf()

plt.show()
