import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")

numeric_cols = [
    "age",
    "studytime",
    "failures",
    "absences",
    "G1",
    "G2",
    "G3"
]

sns.pairplot(
    df[numeric_cols]
)

plt.show()


corr = df[numeric_cols].corr()

plt.figure(figsize=(10, 8))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Matrix")
plt.show()