# Load the Pandas libraries with alias 'pd'
import pandas as pd
from sklearn import linear_model

df = pd.read_csv("times.csv", sep="\t")

X = df[[ "A", "B", "C" ]]
Y = df[[ "TIME" ]]

regr = linear_model.LinearRegression()
regr.fit(X, Y)

print('Intercept: \n', regr.intercept_)
print('Coefficients: \n', regr.coef_)

print(X.head())
print(Y.head())