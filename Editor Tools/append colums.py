import pandas as pd

# Load the CSV file
df = pd.read_csv("./data/over-ear sensitivity official.csv")

# Add a new column 'date' with all values set to '2024-06-15'
df["date"] = "2024-06-15"

# Save the modified DataFrame back to the CSV file
df.to_csv("./data/over-ear sensitivity official modify.csv", index=False)
