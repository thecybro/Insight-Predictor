# import pandas as pd

# file = "storage/changes.csv"

# threshold = 0.005

# df = pd.read_csv(file)

# results = df["result"].values.tolist()

# exceeded = []
# notexceeded = []

# i = 1
# j = 1
# for result in results:
#     if result >= threshold:
#         exceeded.append(result)
#     if result < threshold:
#         notexceeded.append(result)

# for ex in exceeded:
#     print(f"{i}. This value met/exceeded threshold: {ex}")
#     i += 1

# print("\n")

# for no in notexceeded:
#     print(f"{j}. This value didn't exceed threshold: {no}")
#     j += 1

for i,aim in enumerate(range(2,10,2), start=1):
    print(i, aim)