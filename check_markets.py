import requests

url = "https://gamma-api.polymarket.com/events"

response = requests.get(url, timeout=30)

data = response.json()

print(f"Total Events: {len(data)}")
print()

for event in data:
    title = event.get("title", "")

    if "weather" in title.lower() \
        or "temperature" in title.lower() \
        or "rain" in title.lower():
        print("=" * 50)
        print("ID:", event.get("id"))
        print("TITLE:", title)
        print("SLUG:", event.get("slug"))
