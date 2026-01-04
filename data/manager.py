import os
import pandas as pd
from math import fabs
import random

file = "data/sample.csv"
file2 = "data/outputs.csv"


if not (os.path.exists(file)):
    with open(file,"w") as f:
        f.write("X,Y\n")

# with open(file,'a') as f:
#     pairs = [(x,y) for x,y in zip(range(6,101), range(12,201,2))]

#     for x,y in pairs:
#         f.write(f"{x},{y}\n")

# total = []
# for i in df["X"].values:
#     total.append(i)

# df = df.drop(df[df["X"]>10].index)
# df.to_csv(file, index=False)

# X = df["X"].values.tolist()
# Y = df["Y"].values.tolist()

def storer(n,Y,X,Xmean,Ymean,bxy,byx,r,varx,vary,covariance):
    with open(file2,'a') as f:
        f.write(f"{n},{Y},{X},{Xmean},{Ymean},{bxy},{byx},{r},{varx},{vary},{covariance}\n")


def data_manager():
    df = pd.read_csv(file) #sample.csv

    X = max(df["X"].values.tolist())
    new_X = X + 1

    new_Y = 2*X + random.randint(-2,+2)
    new_Y = new_Y

    df.loc[len(df)] = [new_X, new_Y]

    # df.loc[len(df), "X"] = new_X
    # df.loc[len(df)-1, "Y"] = new_Y

    df.to_csv(file, index=False)

    return {
        "new_X":new_X,
        "new_Y":new_Y
        }