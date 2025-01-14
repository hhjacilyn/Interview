import sqlite3
import pandas as pd
import os

# Step 1: Define the database path
folder = r"C:\Users\jacil\Desktop\Interview\Python"
db_name = "financial_data.db"
db_path = os.path.join(folder, db_name)

# Check if the database file exists
if not os.path.exists(db_path):
    raise FileNotFoundError(f"Database file '{db_path}' not found.")

# Step 2: Connect to the database
conn = sqlite3.connect(db_path)

# Step 3: Query the `financials` table
query = "SELECT * FROM financials"
df = pd.read_sql_query(query, conn)

# Step 4: Display the data using Pandas
print("Data from the financials table:")
print(df)

# Step 5: Example Pandas manipulations
# Filter accounts with balance > $10,000
high_balance_accounts = df[df['balance'] > 10000]
print("\nAccounts with balance > $10,000:")
print(high_balance_accounts.to_string(index=False))

# Find the account with the highest balance
max_balance = df['balance'].max()
highest_balance_account = df[df['balance'] == max_balance][['account']]
print("\nAccount with the highest balance:")
print(highest_balance_account.to_string(index=False, header=False))  

# Step 6: Close the connection
conn.close()