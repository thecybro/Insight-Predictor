import pandas as pd
import os

file = "storage/outputs.csv"
file2 = "storage/changes.csv"

# df = pd.read_csv(file)

if not(os.path.exists(file)):
    with open(file, 'w') as f:
        f.write("n,Y,X,Xmean,Ymean,bxy,byx,r,var.x,var.y,covariance\n")

def storer(n,Y,X,Xmean,Ymean,bxy,byx,r,varx,vary,covariance):
    with open(file,'a') as f:
        f.write(f"{n},{Y},{X},{Xmean},{Ymean},{bxy},{byx},{r},{varx},{vary},{covariance}\n")

def calculator(i):
    if i >= 0:
        i = int(i)
        df = pd.read_csv(file)
        df2 = pd.read_csv(file2)

        values = df["X"].values.tolist()

        result = abs(values[i+1] - values[i])
        
        df2.loc[i, "result"] = result
        df2.to_csv(file2, index=False)

        return {"result":result}

    else:
        return 0
    
