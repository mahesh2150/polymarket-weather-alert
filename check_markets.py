import requests
import json

slug = "highest-temperature-in-taipei-on-june-9-2026"

url = f"https://gamma-api.polymarket.com/events/slug/{slug}"

response = requests.get(url, timeout=30)

print("STATUS:", response.status_code)

try:
    print(json.dumps(response.json(), indent=2)[:5000])
except Exception as e:
    print(response.text[:2000])
