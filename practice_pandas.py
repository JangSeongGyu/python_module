import pandas as pd
df = pd.read_csv("./titanic.csv")

for row in zip(df["Age"],["Pclass"]):
    print(row)
    