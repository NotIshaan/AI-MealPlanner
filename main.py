import requests
import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from database import recipes_collection  # Import MongoDB collection

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Meal Planner API is running!"}

# Load API key from .env file
load_dotenv()
API_KEY = os.getenv("API_KEY")
API_URL = "https://api.spoonacular.com/recipes/complexSearch"

@app.get("/recipes")
async def get_recipes(query: str = "chicken"):
    # Check if recipes already exist in MongoDB
    stored_recipes = await recipes_collection.find_one({"query": query})
    if stored_recipes:
        return stored_recipes["data"]  # Return stored recipes

    # Fetch from Spoonacular API
    params = {"query": query, "apiKey": API_KEY}
    response = requests.get(API_URL, params=params)

    if response.status_code != 200:
        raise HTTPException(status_code=500, detail="Failed to fetch recipes")

    recipes = response.json()

    # Store fetched recipes in MongoDB
    await recipes_collection.insert_one({"query": query, "data": recipes})

    return recipes
