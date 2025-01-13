import json
from pymongo import MongoClient

# Step 1: Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/") # default localhost
db = client["financial_database"]  # create or connect to the database
collection = db["financials"]  # create or connect to the collection

# Step 2: Drop the collection if already exists
collection.drop()

# Step 3: Load JSON data into MongoDB
with open("financials.json", 'r') as file:
    data = json.load(file)   # read the JSON file
    collection.insert_many(data)   # inset the data into the MongoDB collection

print("Data successfully inserted into MongoDB!")


# Step 4: Query data using pymongo
print("\nALL records:")
for record in collection.find():
    print(record)


print("\nBalances greater than $5000:")
for record in collection.find({"balance": {"$gt": 5000}}):   # $gt: greater than
    print(record)

# _id: None - no grouping key is used, all records are treated as a single group
pipeline = [{"$group": {"_id": None, "total_balance": {"$sum": "$balance"}}}]
result = list(collection.aggregate(pipeline))  # convert the aggregation result into a list (list of dictionaries)
print(f"\nTotal balance: {result[0]['total_balance']}")


# Step 5: Close the connection
client.close()