import pandas as pd

from engine.stats import train_model, predict_x

from data.manager import data_manager, storer

from storage.formulae import bxy, byx
from storage.manager import calculator


file = "data/sample.csv"
file2 = "data/outputs.csv"
file3 = "storage/changes.csv"
file4 = "storage/getaway.csv"

df = pd.read_csv(file)

X = df["X"].values.tolist()
Y = df["Y"].values.tolist()


print(f"X values: {X}")
print(f"\nY values: {Y}\n")


model = train_model(X, Y)

row = 0

added = 25

n = model["n"]

for i in range(n+1, n+added+1):
    y = 6

    if n == 5:
        x = predict_x(model, y)

        print(f"\nWhen Y is {y} and n is {n},\nX is:{x}\nbxy is:{model['bxy']}")

        storer(i-1,y,x,model['xmean'], model['ymean'], model['bxy'], model['byx'], model['r'], model['xvariance'], model['yvariance'], model['covariance'])

    new_data = data_manager()

    print(f"\nAdded following data to sample.csv:\nX:{new_data["new_X"]}\nY:{new_data["new_Y"]}")

    df = pd.read_csv(file) #sample.csv
    df2 = pd.read_csv(file3) #changes.csv

    X = df["X"].values.tolist()
    Y = df["Y"].values.tolist()

    print(f"X values: {X}")
    print(f"\nY values: {Y}\n")

    model = train_model(X, Y)
    n = model["n"]
    read_row = n-5
    write_row = n-6

    x = predict_x(model, y)

    print(f"\nWhen Y is {y} and n is {n},\nX is:{x}\nbxy is:{model['bxy']}")

    storer(i,y,x,model['xmean'], model['ymean'], model['bxy'], model['byx'], model['r'], model['xvariance'], model['yvariance'], model['covariance'])


    if write_row >= 0:
        calculate = calculator(read_row, write_row)

        print(f"\nChange of {calculate["result"]} in bxy added to row: {calculate["write_row"]} in 'changes.csv'\n")
