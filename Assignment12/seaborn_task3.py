import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="absences",
    bins=20
)

plt.title("Distribution of Absences")
plt.xlabel("Absences")
plt.ylabel("Frequency")
plt.show()

plt.figure(figsize=(8, 5))

sns.kdeplot(
    data=df,
    x="absences",
    fill=True
)

plt.title("KDE Plot of Absences")
plt.xlabel("Absences")
plt.ylabel("Density")
plt.show()


plt.figure(figsize=(8, 5))

sns.rugplot(
    data=df,
    x="absences"
)

plt.title("Rug Plot of Absences")
plt.xlabel("Absences")
plt.show()

plt.figure(figsize=(8, 5))

sns.histplot(
    data=df,
    x="absences",
    bins=20,
    kde=True
)

plt.title("Histogram + KDE of Absences")
plt.xlabel("Absences")
plt.ylabel("Frequency")
plt.show()