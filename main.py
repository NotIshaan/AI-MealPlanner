import requests
import os
from dotenv import load_dotenv
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Meal Planner API is running!"}

load_dotenv()  # Load API key from .env file

API_KEY = os.getenv("API_KEY")
API_URL = "https://api.spoonacular.com/recipes/complexSearch"

@app.get("/recipes")
def get_recipes(query: str = "chicken"):
    params = {"query": query, "apiKey": API_KEY}
    response = requests.get(API_URL, params=params)
    return response.json()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
