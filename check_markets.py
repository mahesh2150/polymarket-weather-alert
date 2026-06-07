import requests

response = requests.get(
    "https://gamma-api.polymarket.com/events",
    params={
        "limit": 100,
        "order": "createdAt",
        "ascending": "false"
    },
    timeout=30
)

events = response.json()

print("EVENTS:", len(events))

for event in events[:20]:
    print("=" * 60)
    print(event.get("createdAt"))
    print(event.get("title"))
    print(event.get("slug"))
