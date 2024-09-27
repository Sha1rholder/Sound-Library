import pandas as pd

paths = [
    "./data/over-ear score cn.csv",
    "./data/over-ear sensitivity official.csv",
]

for path in paths:
    sort = pd.read_csv(path, dtype=str)
    sort.sort_values(by=["brand", "model"], ascending=[
                     True, True], inplace=True)
    sort.to_csv(path, index=False)
