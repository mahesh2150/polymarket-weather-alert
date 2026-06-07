import requests

print("Checking Polymarket...")

url = "https://gamma-api.polymarket.com/events"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)

data = response.json()

print("Events Found:", len(data))
