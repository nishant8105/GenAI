import pandas as pd

students = {
    "Name" : ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    'Marks' : [78, 85, 90, 66, 72],
    "Subject" : ["Maths", "Maths", "Science", "Science", "Math"]
}

df = pd.DataFrame(students)

print("First 3 rows\n",df.head(3))
print("Last 2 rows\n",df.tail(2))
print(f"Dataframe shape : {df.shape},\n Column names : {df.columns}")