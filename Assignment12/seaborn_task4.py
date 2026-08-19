import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 6))

sns.histplot(
    data=df,
    x="absences",
    y="G3",
    bins=20
)

plt.title("Bivariate Histogram: Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade (G3)")
plt.show()

plt.figure(figsize=(8, 6))

sns.kdeplot(
    data=df,
    x="absences",
    y="G3",
    fill=True
)

plt.title("Bivariate KDE: Absences vs Final Grade")
plt.xlabel("Absences")
plt.ylabel("Final Grade (G3)")
plt.show()