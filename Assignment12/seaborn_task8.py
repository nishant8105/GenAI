import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("student_data.csv")

sns.set_theme(style="whitegrid")


g = sns.FacetGrid(
    df,
    col="sex"
)

g.map_dataframe(
    sns.scatterplot,
    x="age",
    y="G3"
)

g.set_axis_labels("Age", "Final Grade (G3)")
g.set_titles("Sex = {col_name}")

plt.show()



g = sns.FacetGrid(
    df,
    col="school"
)

g.map_dataframe(
    sns.scatterplot,
    x="age",
    y="G3"
)

g.set_axis_labels("Age", "Final Grade (G3)")
g.set_titles("School = {col_name}")

plt.show()

sns.relplot(
    data=df,
    x="G2",
    y="G3",
    hue="sex",
    col="school",
    kind="scatter"
)

plt.show()

sns.catplot(
    data=df,
    x="school",
    y="G3",
    hue="sex",
    kind="box"
)

plt.show()

sns.displot(
    data=df,
    x="G3",
    hue="sex",
    kind="hist",
    bins=10
)

plt.show()