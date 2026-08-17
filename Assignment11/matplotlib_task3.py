import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart_Sales.csv")

store_sales = df.groupby("Store")["Weekly_Sales"].mean()
# Vertical bar chart
plt.figure(figsize=(12, 6))
plt.bar(store_sales.index, store_sales.values)

plt.title("Average Weekly Sales by Store")
plt.xlabel("Store Number")
plt.ylabel("Average Weekly Sales")
plt.show()


# 2. Horizontal bar chart
plt.figure(figsize=(10, 12))
plt.barh(store_sales.index, store_sales.values)

plt.title("Average Weekly Sales by Store")
plt.xlabel("Average Weekly Sales")
plt.ylabel("Store Number")

plt.show()