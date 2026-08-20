import pandas as pd
from sklearn.preprocessing import LabelEncoder

# importing clean dataset with no missing values
df =pd.read_csv("clean_student.csv")


categorical_cols = df.select_dtypes(include=['string', "object"]).columns

# Label encoding to categorical columns
le = LabelEncoder()

for col in categorical_cols:
    df[col] = le.fit_transform(df[col])

print(df.head())

# seperate feature and target columns
feature = df.drop("exam_score", axis=1)
target = df['exam_score']

print(feature.head())
print(target.head())