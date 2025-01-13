import csv
import sqlite3
import pandas as pd

# Step 1: Connect to SQLite
conn = sqlite3.connect("example_sql.db")

# create a cursor object tied to the database connection (conn).
# then use the cursor to send SQL queries and fetch results
cursor = conn.cursor()


# Step 2: Drop the existing table if it exists
cursor.execute("DROP TABLE IF EXISTS employees")


# Step 3: create a table
cursor.execute("""
CREATE TABLE IF NOT EXISTS employees (
    id INTEGER PRIMARY KEY,
    name TEXT,
    department TEXT,
    salary INTEGER
    )
""")


# Step 4: insert data

# a) execute: insert single row
# cursor.execute("""
#     INSERT INTO employees (id, name, department, salary)
#     VALUES (?, ?, ?, ?)
# """, (1, 'Alice', 'HR', 50000))

# b) executemany: insert multiple rows
# data = [
#     (1, "Alice", "Engineering", 80000),
#     (2, "Bob", "HR", 50000),
#     (3, "Charlie", "Finance", 60000),
#     (4, "David", "Engineering", 90000)
# ]

# cursor.executemany("""
# INSERT INTO employees (id, name, department, salary)
# VALUES (?,?,?,?)
# """, data)


# Step 4: read data from CSV file
csv_file_path = r"C:\Users\jacil\Desktop\Interview\Python\employees.csv"
with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    cursor.executemany("""
        INSERT INTO employees (id, name, department, salary)
        VALUES (?,?,?,?)
    """, reader)


# Step 5: Commit and close
conn.commit()
print("SQLite database created!")


# Step 6: Use Pandas to query data from database
query = "SELECT * FROM employees"
df = pd.read_sql_query(query, conn)

print("\nData from the database:")
print(df)


# Step 7: data manipulation using Pandas
high_salary_employees = df[df['salary'] > 60000]
print("\nEmployees with salary > 60,000:")
print(high_salary_employees.to_string(index=False))  # remove the index of each row

max_salary = df['salary'].max()
highest_salary_employee = df[df['salary'] == max_salary][['name']]
print("\nEmployee with the highest salary:")
print(highest_salary_employee.to_string(index=False, header=False))  # remove the header


# Step 8: close the connection
conn.close()