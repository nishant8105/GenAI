import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Walmart_Sales.csv")

category_counts = df["Holiday_Flag"].map({
    0: "Non-Holiday",
    1: "Holiday"
}).value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    category_counts.values,
    labels=category_counts.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Share of Holiday vs Non-Holiday Sales Records")

plt.tight_layout()
plt.show()