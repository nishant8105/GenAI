import pandas as pd

students = {
    "Name" : ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    'Marks' : [78, 85, 90, 66, 72],
    "Subject" : ["Maths", "Maths", "Science", "Science", "Maths"]
}

df = pd.DataFrame(students)

avg_marks_per_subject = df.groupby("Subject")["Marks"].mean()
print(avg_marks_per_subject)


no_student_per_subject = df.groupby("Subject")["Name"].count()
print(no_student_per_subject)

max_marks_per_subject = df.groupby("Subject")["Marks"].max()
print(max_marks_per_subject)