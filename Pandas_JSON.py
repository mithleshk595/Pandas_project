import pandas as pd 

df = pd.read_json("data_json")

print(df.to_string())
