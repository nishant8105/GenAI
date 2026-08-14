import pandas as pd

series = pd.Series([78, 85, 90, 66, 72])

print(series.max())
print(series.min())
print(series.sum())
print(series.mean())


result = series.apply(lambda x: "Pass" if x >= 70 else "Fail")
print(result)

print((result == "Pass").sum())