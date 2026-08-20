import pandas as pd

# Kaggle dataset link https://www.kaggle.com/datasets/lainguyn123/student-performance-factors

df =pd.read_csv("student.csv")

# print shape of dataset
print(df.shape)

# print columns names
print(df.columns.tolist())

# print first 5 rows
print(df.head(5))

# print dataset information
print(df.info())

# print discriptive statistics
print(df.describe().T)

print("Converting file for task2 into json")
df.to_json("data.json", index=False)