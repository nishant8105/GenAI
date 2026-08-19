import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")


plt.figure(figsize=(8, 5))

sns.barplot(
    data=df,
    x="school",
    y="G3"
)

plt.title("Average Final Grade by School")
plt.xlabel("School")
plt.ylabel("Average Final Grade")
plt.show()

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="school",
    y="G3"
)

plt.title("Final Grade by School - Box Plot")
plt.xlabel("School")
plt.ylabel("Final Grade (G3)")
plt.show()

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=df,
    x="school",
    y="G3"
)

plt.title("Final Grade by School - Violin Plot")
plt.xlabel("School")
plt.ylabel("Final Grade (G3)")
plt.show()


plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="school"
)

plt.title("Number of Students by School")
plt.xlabel("School")
plt.ylabel("Number of Students")
plt.show()