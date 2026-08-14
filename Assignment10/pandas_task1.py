import pandas as pd

marks = [78, 85, 90, 66, 72]
series = pd.Series(marks)

print("Series: ",series.values)
print("Index: ", series.index)
print("Data types: ",series.dtypes)
print("First element: ", series.iloc[0])
print("Last element:\n", series.iloc[-2:])