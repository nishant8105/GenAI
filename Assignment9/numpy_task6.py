import numpy as np

marks = np.array([78, 85, 90, 66, 72, 88, 95, 60])

print("Sort: ", np.sort(marks))
print("25th percentile: ", np.quantile(marks, q=0.25))
print("50th percentile: ", np.quantile(marks, q=0.50))
print("75th percentile: ", np.quantile(marks, q=0.75))
above_mean = marks[marks > np.mean(marks)]
print("Student scored above the mean marks: ", above_mean)