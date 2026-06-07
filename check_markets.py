import requests

url = "https://gamma-api.polymarket.com/events"

response = requests.get(
    url,
    params={
        "limit": 100
    },
    timeout=30
)

print("Status:", response.status_code)

events = response.json()

print("Events:", len(events))

for event in events:
    title = event.get("title", "")

    if "temperature" in title.lower():
        print("=" * 60)
        print("ID:", event.get("id"))
        print("TITLE:", title)
        print("CREATED:", event.get("createdAt"))
        print("SLUG:", event.get("slug"))
