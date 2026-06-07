import requests
import json

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(url, timeout=30)

print("Status:", response.status_code)

data = response.json()

print("Markets Found:", len(data))

print("\nFIRST MARKET:\n")

print(json.dumps(data[0], indent=2))
