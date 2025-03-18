from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["mealplanner"]
collection = db["users"]

print("MongoDB connected:", client.list_database_names())
