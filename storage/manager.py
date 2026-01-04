import pandas as pd
import os

file = "data/sample.csv"
file2 = "data/outputs.csv"
file3 = "storage/changes.csv"
file4 = "storage/getaway.csv"


if not(os.path.exists(file2)):
    with open(file2, 'w') as f:
        f.write("n,Y,X,Xmean,Ymean,bxy,byx,r,var.x,var.y,covariance\n")

if not(os.path.exists(file4)):
    with open(file3, 'w') as f:
        f.write("Stabilized n,Current n\n")

def calculator(read_row, write_row):
    df = pd.read_csv(file2) #outputs.csv
    df2 = pd.read_csv(file3) #changes.csv


    value1 = df.loc[read_row-1,"bxy"]
    value2 = df.loc[read_row,"bxy"]

    result = abs(value2 - value1)

    df2.loc[write_row] = [write_row+1, f"Δ{write_row+6} = |bxy{write_row+6} − bxy{write_row+5}|", result]

    df2.to_csv(file3, index=False)

    return {
    "write_row": write_row,
    "result":result
    }

    
def getaway_storer(stabilized_n, current_n):
    df = pd.read_csv(file2)

    threshold = 0.01
    results = df["result"].values.tolist()
    