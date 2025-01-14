import pandas as pd
import os
from datetime import datetime

# Step 1: Pick today's file dynamically
today = datetime.today().strftime('%Y%m%d')
folder = r"C:\Users\jacil\Desktop\Interview\Python"
file_name = f"financials_{today}.csv"
csv_file_path = os.path.join(folder, file_name)

# Check if the file exists
if not os.path.exists(csv_file_path):
    raise FileNotFoundError(f"File '{csv_file_path}' not found.")

# Step 2: Load the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file_path)

# Step 3: Manipulate data using Pandas
print("\nData from the file:")
print(df)

# Filter accounts with balance > $10,000
high_balance_accounts = df[df['balance'] > 10000]
print("\nAccounts with balance > $10,000:")
print(high_balance_accounts.to_string(index=False))

# Find the account with the highest balance
max_balance = df['balance'].max()
highest_balance_account = df[df['balance'] == max_balance][['account']]
print("\nAccount with the highest balance:")
print(highest_balance_account.to_string(index=False, header=False))  # Display without header



# Optional: Save modified data back to the same location
output_file_name = "modified_financials.csv"
output_file_path = os.path.join(folder, output_file_name)  # Save in the same location

# Save the DataFrame to a CSV file without index
df.to_csv(output_file_path, index=False)

print(f"\nModified data saved to: {output_file_path}")
