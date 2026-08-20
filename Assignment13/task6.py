import pandas as pd
import re
# read dataset file
df = pd.read_csv("student.csv")

# find missing value
print(df.isnull().sum())

# filling missing value of Teacher_Quality with mode
df["Teacher_Quality"] = df["Teacher_Quality"].fillna(df["Teacher_Quality"].mode()[0])
print("Null values in Teacher Quality", df["Teacher_Quality"].isnull().sum())


# Filling missing value of Parental_Education_Level with Unknown
df["Parental_Education_Level"] = df["Parental_Education_Level"].fillna(df["Parental_Education_Level"].mode()[0])
print("Null values in parental Education level", df["Parental_Education_Level"].isnull().sum())


# Filling missing value of Distance_from_Home with mode
df["Distance_from_Home"] = df["Distance_from_Home"].fillna(df["Distance_from_Home"].mode()[0])
print("Null values in distance from home", df["Distance_from_Home"].isnull().sum())

# print duplicate values
print("Duplicate values",df.duplicated().sum())


# renaming columns in lowercase and snake_case
df.columns = [
    re.sub(r'[^a-z0-9]+', '_', col.lower()).strip('_')
    for col in df.columns
]

print(df.columns)

df.to_csv("clean_student.csv", index=False)
print("Data types before explicit conversion:")
print(df.dtypes)
# each columns are having correct datatypes