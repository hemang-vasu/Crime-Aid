import pandas as pd

v = pd.read_csv("predTimes.csv")
print(v.dtypes)
vv = pd.read_csv("gTimes.csv")
print(vv.dtypes)