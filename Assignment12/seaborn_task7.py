import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))

sns.regplot(
    data=df,
    x="G2",
    y="G3"
)

plt.title("Regression Plot: G2 vs G3")
plt.xlabel("Second Period Grade (G2)")
plt.ylabel("Final Grade (G3)")
plt.show()


sns.lmplot(
    data=df,
    x="G2",
    y="G3",
    hue="sex"
)

plt.xlabel("Second Period Grade (G2)")
plt.ylabel("Final Grade (G3)")
plt.show()