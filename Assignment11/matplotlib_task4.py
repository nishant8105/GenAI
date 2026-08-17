import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

df = pd.read_csv("Walmart_Sales.csv")

df["Date"] = pd.to_datetime(df["Date"], dayfirst=True, errors="coerce")

df["Year"] = df["Date"].dt.year

yearly_sales = df.groupby("Year")["Weekly_Sales"].sum()

years = yearly_sales.index.astype(str)
sales = yearly_sales.values
x = np.arange(len(years))

width = 0.6

plt.figure(figsize=(10, 6))

plt.bar(
    x,
    sales,
    width=width,
    align="center",
    label="Total Sales"
)

plt.title("Total Walmart Sales by Year")
plt.xlabel("Year")
plt.ylabel("Total Weekly Sales")


plt.legend()

plt.show()