import numpy as np

sales = np.array([1200, 1500, 900, 2000, 1800, 1700, 1600])

print("Total weekly sales: ", np.sum(sales))
print(f"Average daily sales: {np.mean(sales):.2f}")
print(f"Highest sale : {np.max(sales)}, and Lowest sale : {np.min(sales)}")
print(f"Standard deviation of sales: {np.std(sales):.2f}")
above_mean = sales[sales > np.mean(sales)]
print("Sales above average: ", above_mean)