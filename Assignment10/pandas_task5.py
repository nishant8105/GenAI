import pandas as pd

students = {
    "Name" : ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    'Marks' : [78, 85, 90, 66, 72],
    "Subject" : ["Maths", "Maths", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)

print("Student dataframe information\n",df.info())
print("Student datafrane discribe\n", df.describe())
print("Head\n", df.head())
print("Tail\n", df.tail())
print(df.sort_values(by = "Marks", ascending=False))
print(df)