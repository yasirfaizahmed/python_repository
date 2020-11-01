from matplotlib import pyplot as plt
import pandas as pd
from sklearn import linear_model

def variance(mean, value):
    return sum((value - mean)**2)/len(value)

def covariace(value1, value2, mean1, mean2):
    return sum((value1 - mean1)*(value2 - mean2))/len(value1)

def predict(x, m, c):
    return m*x + c

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

######using sklear
plt.subplot(122)
plt.scatter(df['area'], df['price'], color='red', marker='+')
plt.plot([100, 4000],[mod.predict([[100]]), mod.predict([[4000]])])

plt.show()
