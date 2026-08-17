import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart_Sales.csv")

df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

df["Year"] = df["Date"].dt.year

sales_by_store_year = (
    df.groupby(["Store", "Year"])["Weekly_Sales"]
      .sum()
      .unstack(fill_value=0)
)

ax = sales_by_store_year.plot(
    kind="bar",
    stacked=True,
    figsize=(14, 7),
    width=0.8
)

ax.set_title(
    "Stacked Total Weekly Sales by Store and Year",
    fontsize=15
)

ax.set_xlabel("Store Number", fontsize=12)
ax.set_ylabel("Total Weekly Sales", fontsize=12)

ax.legend(title="Year")

plt.show()