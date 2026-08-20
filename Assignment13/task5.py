import pandas as pd

# read csv file form task 1
df = pd.read_csv("student.csv")

# Print columns data types
print(df.dtypes)

# numerical columns
numeric_cols = df.select_dtypes(include="number")

print(numeric_cols.columns)

# categorical columns
categorical_col = df.select_dtypes(include='string')
print(categorical_col.columns)


# missing values per columns
print(df.isnull().sum())

print(df.head(5))

# print dataset information
print(df.info())

# print discriptive statistics
print(df.describe().T)

# print shape of dataset
print(df.shape)