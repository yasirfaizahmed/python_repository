#Refence links
#https://dhirajkumarblog.medium.com/linear-regression-without-sklearn-from-scratch-5c83b46642f8


############     USING LEAST SQUARE FIT ##############

from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model

def variance(mean, value):
    return sum((value - mean)**2)/len(value)

def covariace(value1, value2, mean1, mean2):
    return sum((value1 - mean1)*(value2 - mean2))/len(value1)

def predict(x, m, c):
    return m*x + c

def R_squared(x, y, y_mean, m, c):
    return (sum((y - predict(x, m, c))**2) / sum((y - y_mean)**2))



df = pd.read_csv("housing_prices0.csv")

mod = linear_model.LinearRegression()
mod.fit(df[['area']], df.price)

mean_price = sum(df['price'])/len(df.price)
#print("mean_price = ",mean_price)
mean_area = sum(df.area)/len(df.area)
#print("mean_area = ", mean_area)


print("variance_area = ", variance(mean_area, df['area']) )
print("variance_price = ", variance(mean_price, df['price']) )
print("co_variance = ",covariace(df['area'], df['price'], mean_area, mean_price))
print("m = ", covariace(df['area'], df['price'], mean_area, mean_price) / variance(mean_area, df['area']))
print("intercept = ", mean_price - covariace(df['area'], df['price'], mean_area, mean_price) / variance(mean_area, df['area']) * mean_area)

print("model coef. = ",mod.coef_)
print("model intercept = ", mod.intercept_)


m = covariace(df['area'], df['price'], mean_area, mean_price) / variance(mean_area, df['area'])
c = mean_price - m*mean_area

########from scratch
plt.subplot(121)
plt.scatter(df['area'], df['price'], color='red', marker='+')
ys = [predict(100, m, c), predict(4000, m, c)]
plt.plot([100, 4000], ys)

######using sklearn
plt.subplot(122)
plt.scatter(df['area'], df['price'], color='red', marker='+')
plt.plot([100, 4000],[mod.predict([[100]]), mod.predict([[4000]])])

print("R squared value = ", R_squared(df['area'], df['price'], mean_price, m, c))

plt.show()


'''
df = pd.read_csv("linear0.csv")
x = df['x'].to_numpy()
y = df['y'].to_numpy()

mean_x = sum(x)/len(x)
mean_y = sum(y)/len(y)

m = covariace(x, y, mean_x, mean_y) / variance(mean_x, x)
c = mean_y - m * mean_x

print("m = ", m)
print("c = ", c)

print("R squared = ", R_squared(x, y, mean_y, m, c))

'''
