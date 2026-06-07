import requests
import json

URL = "https://gamma-api.polymarket.com/events/keyset"

params = {
    "limit": 100,
    "tag_slug": "weather",
    "closed": "false",
    "order": "volume24hr",
    "ascending": "false"
}

print("Fetching weather events...")

response = requests.get(
    URL,
    params=params,
    timeout=30
)

response.raise_for_status()

events = response.json()

print(f"Weather Events Found: {len(events)}")
print()

for i, event in enumerate(events[:20], start=1):
    print("=" * 80)
    print(f"EVENT #{i}")
    print("ID:", event.get("id"))
    print("TITLE:", event.get("title"))
    print("SLUG:", event.get("slug"))
    print("CREATED:", event.get("createdAt"))
    print("ACTIVE:", event.get("active"))
    print("CLOSED:", event.get("closed"))
    print()
