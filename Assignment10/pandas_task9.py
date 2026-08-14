import pandas as pd

sales = {
    'Day': ["Mon", "Tue", "Wed", "Thu", "Fri"],
    'Revenue' : [1200, 1500, 900, 2000, 1800]
}

df = pd.DataFrame(sales)

# total revenue
print(df["Revenue"].sum())

# Average revenue
print(df["Revenue"].mean())

# Day with highest revenue
highest_day = df.loc[df['Revenue'].idxmax()]
print(highest_day)

# Day where revenue > average
above_avg = df[df["Revenue"] > df["Revenue"].mean()]
print(above_avg)

import matplotlib.pyplot as plt
df.plot(kind="bar", x="Day", y="Revenue")
plt.show()