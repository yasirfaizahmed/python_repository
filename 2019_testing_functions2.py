from statistics import mean
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from sklearn import datasets

iris = datasets.load_iris()

#Number of Attributes: 4 numeric, predictive attributes and the class\n    :Attribute Information:\n        - sepal length in cm\n        - sepal width in cm\n        - petal length in cm\n        - petal width in cm\n

#sepal length:   4.3  7.9   5.84   0.83    0.7826\n    sepal width:    2.0  4.4   3.05   0.43   -0.4194\n    petal length:   1.0  6.9   3.76   1.76    0.9490  (high!)\n    petal width:    0.1  2.5   1.20   0.76    0.9565  (high!)\n
#[[5.1 3.5 1.4 0.2]
# [4.9 3.  1.4 0.2]
# [4.7 3.2 1.3 0.2]
# [4.6 3.1 1.5 0.2]
# [5.  3.6 1.4 0.2]
# [5.4 3.9 1.7 0.4]
# [4.6 3.4 1.4 0.3]]

sl = []
sw = []
pl = []
pw = []
for i in iris.data:
    sl.append(i[0])
    sw.append(i[1])
    pl.append(i[2])
    pw.append(i[3])
print(sl)




