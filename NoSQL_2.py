import json
import os
import pandas as pd
from datetime import datetime
from pymongo import MongoClient


# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/") # default localhost
db = client["financial_database"]  # create or connect to the database
collection = db["financials"]  # create or connect to the collection

# Step 2: Drop the collection if already exists
collection.drop()

# Step 3: Dynamically load today's JSON file into MongoDB
folder = r"C:\Users\jacil\Desktop\Interview\Python"
today = datetime.today().strftime('%Y%m%d')
file_name = f"financials_{today}.json"

file_path = os.path.join(folder, file_name)

# check if the file exists
if not os.path.exists(file_path):
    raise FileNotFoundError(f"File '{file_path}' not found.")
else:
    with open(file_path, 'r') as file:
        data = json.load(file)   # read the JSON file
        collection.insert_many(data)   # inset the data into the MongoDB collection
    print("Data successfully inserted into MongoDB!")


# Step 4: Load JSON into a Pandas DataFrame for manipulation
df = pd.DataFrame(data)

print("\nALL records:")
print(df)


print("\nBalances greater than $5000:")
filtered_df = df[df['balance'] > 5000]
print(filtered_df.drop(columns=['_id']).to_string(index=False))

# _id: None - no grouping key is used, all records are treated as a single group
total_balance = df['balance'].sum()
print(f"\nTotal balance: {total_balance}")


# Step 5: Close the connection
client.close()