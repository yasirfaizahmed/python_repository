import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn import linear_model


def mean_squared_error(y, y_pred):
    return sum((y - y_pred)**2) / len(y)


df = pd.read_csv("test.csv")
df_np = df.to_numpy()
x = df_np[:, 0]
y = df_np[:, 1]

m, c = 0, 0
lr = 0.00001
epoch = 1000
n = len(x)

plt.title("Gradiant descent")

for i in range(epoch):
    Y_pred = m * x + c
    D_m = (-2 / n) * sum(x * (y - Y_pred))
    D_c = (-2 / n) * sum(y - Y_pred)
    m = m - lr * D_m
    c = c - lr * D_c
    plt.subplot(121)
    plt.clf()
    plt.scatter(x, y, color='red', marker='+')
    plt.plot([x.min(), x.max()], [m * x.min() + c, m * x.max() + c])


plt.show()

print(m, c)
