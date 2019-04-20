from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import datasets

#sepal length:   4.3  7.9   5.84   0.83    0.7826\n    sepal width:    2.0  4.4   3.05   0.43   -0.4194\n    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\n    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\n

iris = datasets.load_iris()
style.use('fivethirtyeight')

sl = []
#sw = []
pl = []
#pw = []
for i in iris.data:
    sl.append(i[0])
    #sw.append(i[1])
    pl.append(i[2])
    #pw.append(i[3])

xs = np.array(sl, dtype=np.float64)
ys = np.array(pl, dtype=np.float64)

def best_fit_slope_and_intercept(xs, ys):
    m = ( mean(xs)*mean(ys) - mean(xs*ys) ) / ( mean(xs)*mean(xs) - mean(xs*xs) )
    b = mean(ys) - m*mean(xs)
    return m, b

m, b = best_fit_slope_and_intercept(xs, ys)
print("slope , y_intercept : ", m, b)


def squared_error(ys_orig, ys_line):
    return sum((ys_line - ys_orig)**2)

def coeffecient_of_determination(ys_orig, ys_line):
    y_mean_line = [mean(ys_orig) for y in ys_orig]
    squared_error_regr = squared_error(ys_orig, ys_line)
    squared_error_y_mean = squared_error(ys_orig, y_mean_line)
    return 1- (squared_error_regr / squared_error_y_mean)



inp = input("Enter what to predict, i.e., sl or pl ?")
if inp=="pl":
    hah1 = input("Enter the sl value :")
    haha1 = int(hah1)
    ppl = m*haha1 + b
    print("predicted petal_length :", ppl)

    plt.scatter(xs, ys)
    y = []
    for i in xs:
        y.append(m * i + b)
    print("accuracy :", (coeffecient_of_determination(ys, y)) * 100)
    plt.plot(xs, y)
    plt.scatter(haha1, ppl, color='r')
    plt.show()


if inp=="sl":
    hah2 = input("Enter the pl value :")
    haha2 = int(hah2)
    psl = (haha2 - b)/m
    print("predicted sepal_length :", psl)

    plt.scatter(xs, ys)
    y = []
    for i in xs:
        y.append(m * i + b)
    print("accuracy :", (coeffecient_of_determination(ys, y)) * 100)
    plt.plot(xs, y)
    plt.scatter(psl, haha2, color='r')
    plt.show()



