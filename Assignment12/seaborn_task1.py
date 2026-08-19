import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")

sns.relplot(
    data=df,
    x="age",
    y="G3",
    hue="sex"
)

plt.title("Age vs Final Grade by Sex")
plt.show()

sns.relplot(
    data=df,
    x="age",
    y="G3",
    hue="sex",
    kind="scatter"
)

plt.title("Scatter Plot: Age vs Final Grade by Sex")
plt.show()