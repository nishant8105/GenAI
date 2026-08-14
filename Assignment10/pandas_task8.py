import pandas as pd
import matplotlib.pyplot as plt
students = {
    "Name" : ["Amit", "Neha", "Rahul", "Sneha", "Pooja"],
    'Marks' : [78, 85, 90, 66, 72],
    "Subject" : ["Maths", "Maths", "Science", "Science", "Maths"]
}

df = pd.DataFrame(students)
# bar graph of name vs marks
df.plot(kind="bar", x="Name", y="Marks")
plt.show()
# line plot of marks
df["Marks"].plot(kind="line", marker='o')
plt.show()
# hist plot of marks
df['Marks'].plot(kind="hist", bins=5)
plt.show()