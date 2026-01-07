import pandas as pd

file = "storage/changes.csv"

threshold = 0.005

# # df = pd.read_csv(file)

# # results = df["result"].values.tolist()

# # exceeded = []
# # notexceeded = []

# # i = 1
# # j = 1
# # for result in results:
# #     if result >= threshold:
# #         exceeded.append(result)
# #     if result < threshold:
# #         notexceeded.append(result)

# # for ex in exceeded:
# #     print(f"{i}. This value met/exceeded threshold: {ex}")
# #     i += 1

# # print("\n")

# # for no in notexceeded:
# #     print(f"{j}. This value didn't exceed threshold: {no}")
# #     j += 1

# # for i,aim in enumerate(range(2,10,2), start=1):
# #     print(i, aim)

# # print(abs(-56-2))

# threshold = 0.005
# k = 5
# validity = 90

# df = pd.read_csv(file)  #changes.csv

# for i,result in enumerate(df["result"].values.tolist(), start=1):
#     if result < threshold and i >= k:
#         converged = True

#     else:
#         converged = False
        
        
# if converged == False:
#     validity *= 0.7

# print(converged)
# print(validity)
k = 5
df = pd.read_csv(file)  #changes.csv
total_n = len(df) + 5 #Cuz starting form 6
i = 0
for result in df["result"].values.tolist():
    if result < threshold:
        print(f"{result} is less than {threshold}")
        i += 1

    else:
        print(f"{result} is NOT less than {threshold}")
        i = 0
        
if i >= k:
    converged_case = True
    converged_n = total_n - i

else:
    converged_case = False
    converged_n = None
    
print(i)
print(converged_case)
print(converged_n)