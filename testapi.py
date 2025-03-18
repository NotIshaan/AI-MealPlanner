import requests

API_KEY = "14e1326e2f244d0ba425210a1375ec6c"
url = f"https://api.spoonacular.com/recipes/random?apiKey={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)
