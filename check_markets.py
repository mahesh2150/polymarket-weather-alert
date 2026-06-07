import requests

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
events = data["events"]

print(f"Weather Events Found: {len(events)}")
print()

for i, event in enumerate(events[:10], start=1):
    print("=" * 80)
    print(f"EVENT #{i}")
    print("ID:", event["id"])
    print("TITLE:", event["title"])
    print("SLUG:", event["slug"])
    print("CREATED:", event["createdAt"])
