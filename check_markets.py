import requests
import json

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(url, timeout=30)

data = response.json()

print(json.dumps(data[0]["events"], indent=2))
