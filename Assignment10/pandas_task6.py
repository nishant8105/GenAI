import pandas as pd

students = {
    "Name" : ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    'Marks' : [78, 85, 90, 66, 72],
    "Subject" : ["Maths", "Maths", "Science", "Science", "Maths"]
}

df = pd.DataFrame(students)

students_above_75 = df[df["Marks"] > 75]
print(f"{students_above_75=}\n")

student_from_maths = df[df["Subject"] == "Maths"]
print(f"{student_from_maths=}\n")

student_above_average = df[df["Marks"] > (df["Marks"].mean())]
print(f"{student_above_average=}\n")

failed_student = df[df["Marks"] < 70]
print(f"{failed_student=}")