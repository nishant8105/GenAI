import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart_Sales.csv")

sales = df["Weekly_Sales"].dropna()

plt.figure(figsize=(10, 6))
plt.hist(
    sales,
    bins=30,
    edgecolor="black",
    alpha=0.7
)

plt.title("Distribution of Weekly Sales")
plt.xlabel("Weekly Sales")
plt.ylabel("Frequency")

plt.grid(axis="y", alpha=0.3)
plt.tight_layout()
plt.show()