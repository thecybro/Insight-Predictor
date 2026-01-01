import os
import pandas as pd
from math import fabs

file = "data/sample.csv"

df = pd.read_csv(file)

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
