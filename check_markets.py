import requests
import json

url = "https://gamma-api.polymarket.com/events/keyset"

response = requests.get(
    url,
    params={
        "limit": 100,
        "tag_slug": "weather",
        "closed": "false",
        "order": "volume24hr",
        "ascending": "false"
    },
    timeout=30
)

response.raise_for_status()

data = response.json()

print("TYPE:", type(data))
print()
print(json.dumps(data, indent=2)[:5000])
