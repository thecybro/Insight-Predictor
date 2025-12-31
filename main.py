import pandas as pd

from engine.stats import mean_displayer, std_dev_displayer, variance_displayer
from engine.stats import covariance_displayer, correlation_coefficient_displayer
from engine.stats import Xfinder, Yfinder
from engine.stats import interpreter, validity_checker

from engine.stats import train_model, predict_x

from storage.formulae import bxy, byx

file = "data/sample.csv"

df = pd.read_csv(file)

X = df["X"].values.tolist()
Y = df["Y"].values.tolist()


X_from_Y = Xfinder(X, Y, 6)
Y_from_X = Yfinder(X, Y, 3)

# b_xy = bxy(X, Y)
# b_yx = byx(X, Y)

print(f"X values: {X}")
print(f"\nY values: {Y}\n")

# print(f"\nValue of X when Y is 6(ymean) is:",X_from_Y)

# print(f"\nValue of Y when X is 3(xmean) is:",Y_from_X)


model = train_model(X, Y)

for i in [6,1500,-5]:
    exp1 = predict_x(model, i)
    print(f"When Y is {i}, X is:{exp1}")