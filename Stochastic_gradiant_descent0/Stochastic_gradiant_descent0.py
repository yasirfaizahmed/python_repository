import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("test.csv")
df_np = df.to_numpy()
x = df_np[:, 0]
y = df_np[:, 1]

lr = 0.0001
epoch = 100
batch_size = 3
m, c = 0, 0
n = len(x)

for i in range(epoch):
    ran_indexes = np.random.randint(0, n, batch_size)
    ran_x = np.take(x, ran_indexes)
    ran_y = np.take(y, ran_indexes)

    f = ran_y - (m*ran_x + c)
    m -= lr * (-2 / batch_size) * (sum(ran_x * f))
    c -= lr * (-2 / batch_size) * (sum(f))
    plt.scatter(x, y, color='red', marker='+')
    plt.plot([x.min(), x.max()], [m * x.min() + c, m * x.max() + c])
    plt.pause(0.1)
    plt.clf()
plt.show()
print("m = ", m)
print("c = ", c)

