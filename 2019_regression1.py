import numpy as np
import panda as pa
import matplotlib.pyplot as plt

plt.rcParams['figure.figsize'] = (20.0, 10.0)

data = pa.read_csv('headerbrain.csv')
print(data.shape)
data.head()