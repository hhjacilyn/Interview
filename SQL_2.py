import csv
from datetime import datetime
import os
import sqlite3
import pandas as pd

# Step 1: Connect to SQLite
conn = sqlite3.connect("financial_data.db")

# create a cursor object tied to the database connection (conn).
# then use the cursor to send SQL queries and fetch results
cursor = conn.cursor()


# Step 2: Drop the existing table if it exists
cursor.execute("DROP TABLE IF EXISTS financials")


# Step 3: create a table
# Real: floating number
cursor.execute("""
CREATE TABLE IF NOT EXISTS financials (
    id INTEGER PRIMARY KEY,
    account TEXT,
    date TEXT,
    balance REAL   
    )
""")


# Step 4: read data from CSV file

# Pick today's file dynamically
today = datetime.today().strftime('%Y%m%d')
folder = r"C:\Users\jacil\Desktop\Interview\Python"  # r: treats \ as literal characters, not as escape for \n, \t
file_name = f"financials_{today}.csv"  # f: allows embedding expressions into strings through {}
csv_file_path = os.path.join(folder, file_name)  # os: ensures code works on different operating systems (path: \ for windows, / for Linus/macOS)

# check if file exists
if not os.path.exists(csv_file_path ):
    raise FileNotFoundError(f"File '{csv_file_path}' not found.")


with open(csv_file_path, 'r') as file:
    reader = csv.reader(file)
    next(reader)  # skip the header row
    cursor.executemany("""
        INSERT INTO financials (id, account, date, balance)
        VALUES (?,?,?,?)
    """, reader)


# Step 5: Commit and close
conn.commit()
print("Financial data imported into SQLite database!")


# Step 6: Use Pandas to query data from database
query = "SELECT * FROM financials"
df = pd.read_sql_query(query, conn)

print("\nData from the database:")
print(df)


# Step 7: data manipulation using Pandas
high_balance_accounts = df[df['balance'] > 10000]
print("\nAccounts with balance > $10,000:")
print(high_balance_accounts.to_string(index=False))  # remove the index of each row

max_balance = df['balance'].max()
highest_balance_account = df[df['balance'] == max_balance][['account']]
print("\nAccount with the highest balance:")
print(highest_balance_account.to_string(index=False, header=False))  # remove the header


# Step 8: close the connection
conn.close()