import pandas as pd

series = pd.Series([78, 85, 90, 66, 72])

print("Add 5 grace marks to all students :\n", series + 5) 
print("Subrtact 2 marks from all student :\n", series - 2)
print("Multiply all marks by 1.05 :\n", series * 1.05)
print("Divide all marks by 2:\n",series / 2)