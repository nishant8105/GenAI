import pandas as pd

# dataset is from kaggle from task1 and converted from csv to json

# importing dataset
json_data = pd.read_json("data.json")

# convert to dataframe
df = pd.DataFrame(json_data)

# print frist 5 rows of dataframe
print(df.head())
