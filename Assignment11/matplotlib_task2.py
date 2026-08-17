import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart_Sales.csv")

plt.scatter(df["Store"], df["Weekly_Sales"])

plt.title("Relationship Between Store and Weekly Sales")
plt.xlabel("Store Number")
plt.ylabel("Weekly Sales")

plt.show()