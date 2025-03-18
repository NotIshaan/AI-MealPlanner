from motor.motor_asyncio import AsyncIOMotorClient

MONGO_URI = "mongodb://localhost:27017"
DB_NAME = "mealplanner"

client = AsyncIOMotorClient(MONGO_URI)
db = client[DB_NAME]
