import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))

sns.lineplot(
    data=df,
    x="age",
    y="G3"
)

plt.title("Age vs Final Grade - Line Plot")
plt.xlabel("Age")
plt.ylabel("Final Grade (G3)")
plt.show()

plt.figure(figsize=(8, 5))

sns.lineplot(
    data=df,
    x="age",
    y="G3",
    marker="o",
    dashes=False
)

plt.title("Age vs Final Grade - Scatter Style Line Plot")
plt.xlabel("Age")
plt.ylabel("Final Grade (G3)")
plt.show()

g = sns.relplot(
    data=df,
    x="age",
    y="G3",
    col="sex",
    kind="line",
    marker="o"
)

g.set_axis_labels("Age", "Final Grade (G3)")
g.set_titles("Sex = {col_name}")

plt.show()
