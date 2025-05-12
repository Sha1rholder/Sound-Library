import pandas as pd

path = "./data/over-ear sensitivity official.csv"
sort = pd.read_csv(path, dtype=str)
sort.sort_values(by=["brand", "model"], ascending=[
    True, True], inplace=True)
sort.to_csv(path, index=False)
