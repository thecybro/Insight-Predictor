import os
import pandas as pd

file = "data/sample.csv"

df = pd.read_csv(file)

if not (os.path.exists(file)):
    with open(file,"w") as f:
        f.write("X,Y\n")

with open(file,'a') as f:
    pairs = [(x,y) for x,y in zip(range(6,101), range(12,201,2))]

    for x,y in pairs:
        f.write(f"{x},{y}\n")

X = df["X"].values.tolist()
Y = df["Y"].values.tolist()
