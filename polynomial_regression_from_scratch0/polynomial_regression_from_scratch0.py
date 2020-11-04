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

    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title(q)
    plt.pause(0.5)
    plt.clf()

plt.show()
