import pandas as pd
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["financial_database"]  # connect to the database
collection = db["financials"]  # connect to the collection

# Step 2: Read data from MongoDB into a Pandas DataFrame
# Query all documents in the "financials" collection
data = list(collection.find())  # Convert cursor to a list of dictionaries

if data:  # Check if there is data in the collection
    # Load into Pandas DataFrame
    df = pd.DataFrame(data)

    # Drop MongoDB's default `_id` column if not needed
    if '_id' in df.columns:
        df.drop(columns=['_id'], inplace=True)

    print("\nALL records:")
    print(df)

    # Filter accounts with balances greater than $5000
    print("\nBalances greater than $5000:")
    filtered_df = df[df['balance'] > 5000]
    print(filtered_df.to_string(index=False))

    # Calculate the total balance
    total_balance = df['balance'].sum()
    print(f"\nTotal balance: {total_balance}")
else:
    print("The collection is empty!")

# Step 3: Close the connection
client.close()