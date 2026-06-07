import requests
import json

print("Checking Polymarket...")

url = "https://gamma-api.polymarket.com/events"

response = requests.get(url, timeout=30)

print("Status Code:", response.status_code)

data = response.json()

print("Events Found:", len(data))

print("\nFIRST EVENT:\n")
print(json.dumps(data[0], indent=2))
