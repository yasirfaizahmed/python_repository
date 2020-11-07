import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

#####################       USING CRAMERS RULE

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


df = pd.read_csv("sample.csv")
np_df = df[['x','y']].to_numpy()
x = np_df[0:, 0]
y = np_df[0:, 1]

#########from scratch
degree = 12     #max degree for the model
coeff = poly_reg(y, x, degree)
predicted = predict_array(degree=degree, coeff=coeff, length=200)

plt.subplot(121)
plt.plot(np.arange(0, 20, 0.1), predicted)
plt.scatter(x, y, color='red', marker='+')

#############using sklearn lib
x = x[:, np.newaxis]
lin = LinearRegression()
lin.fit(x, y)
poly = PolynomialFeatures(degree=degree)
x_poly = poly.fit_transform(x)
poly.fit(x_poly, y)
lin2 = LinearRegression()
lin2.fit(x_poly, y)

plt.subplot(122)
plt.plot(x, lin2.predict(poly.fit_transform(x)), color = 'red')

print(y)

plt.show()
