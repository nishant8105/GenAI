import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart_sales.csv")

df['Date'] = pd.to_datetime(df['Date'], dayfirst=True)

monthly_sales = df.groupby(df["Date"].dt.to_period("M"))["Weekly_Sales"].sum()

monthly_sales.plot(kind="line", marker="o")

plt.title("Walmart sales trend over months")
plt.xlabel("Months")
plt.ylabel("Total sales")

plt.show()