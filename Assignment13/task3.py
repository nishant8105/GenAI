# import library for creating SQL database
import sqlite3
import pandas as pd

# connect database
conn = sqlite3.connect("sample.db")

cursor = conn.cursor()

# createing table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employee (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary REAL
)
""")

# Adding entries in database
employees = [
    (1, "Rahul", "IT", 55000),
    (2, "Priya", "HR", 45000),
    (3, "Amit", "Finance", 60000),
    (4, "Sneha", "IT", 65000),
    (5, "Rohit", "Marketing", 50000)
]

cursor.executemany("""
INSERT OR IGNORE INTO employee
(id, name, department, salary)
VALUES (?, ?, ?, ?)
""", employees)

conn.commit()

# query to extract dataframe from dataset
query = "SELECT * FROM employee"

df = pd.read_sql_query(query, conn)

print(df)

conn.close()