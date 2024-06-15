import pandas as pd

df = pd.read_csv("./data/over-ear assessments cn.csv")
df.insert(3, "sound", pd.NA)
df.insert(4, "build", pd.NA)
df.insert(5, "comfort", pd.NA)
df.to_csv("./data/over-ear assessments cn.csv", index=False)
