import pandas as pd

from engine.stats import mean_displayer, std_dev_displayer, variance_displayer
from engine.stats import covariance_displayer, correlation_coefficient_displayer
from engine.stats import Xfinder, Yfinder
from engine.stats import interpreter, validity_checker

from engine.stats import train_model, predict_x

from storage.formulae import bxy, byx
from storage.manager import storer, calculator

file = "data/sample.csv"

df = pd.read_csv(file)

X = df["X"].values.tolist()
Y = df["Y"].values.tolist()


X_from_Y = Xfinder(X, Y, 6)
Y_from_X = Yfinder(X, Y, 3)

b_xy = bxy(X, Y)
# b_yx = byx(X, Y)

print(f"X values: {X}")
print(f"\nY values: {Y}\n")

# print(f"\nValue of X when Y is 6(ymean) is:",X_from_Y)

# print(f"\nValue of Y when X is 3(xmean) is:",Y_from_X)


model = train_model(X, Y)

row = 0

n = model["n"]
row = n-6


for i in [6]:
    x = predict_x(model, i)
    storer(model["n"],i,x,model['xmean'], model['ymean'], model['bxy'], model['byx'], model['r'], model['variance'], "", model['covariance'])
    print(f"When Y is {i} and n is {n}, X is:{x}")

    calculate = calculator(row)
    if calculate != 0:
        print(f"Change {calculate["result"]} added to row: {int(row)}")
