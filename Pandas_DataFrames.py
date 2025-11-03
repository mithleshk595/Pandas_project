import pandas as pd

data = {
    "colories": [420, 380, 390],
    "Duration": [50, 40, 45]
}

#load data into a Dataframe object:
df = pd.DataFrame(data)
print(df)

