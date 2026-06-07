import requests

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(url, timeout=30)

data = response.json()

print("FIELDS:")
print(list(data[0].keys()))
