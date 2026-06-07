import requests
import json
import os

SEEN_FILE = "seen_events.json"

# Load previously seen event IDs
if os.path.exists(SEEN_FILE):
    with open(SEEN_FILE, "r") as f:
        seen_ids = set(json.load(f))
else:
    seen_ids = set()

response = requests.get(
    "https://gamma-api.polymarket.com/events",
    params={
        "limit": 100
    },
    timeout=30
)

response.raise_for_status()

events = response.json()

new_seen_ids = set(seen_ids)

new_weather_events = []

for event in events:

    event_id = str(event.get("id"))
    title = event.get("title", "")
    slug = event.get("slug", "")

    title_lower = title.lower()
    slug_lower = slug.lower()

    is_weather = (
        "highest temperature" in title_lower
        or "temperature" in title_lower
        or "highest-temperature" in slug_lower
    )

    if not is_weather:
        continue

    if event_id not in seen_ids:
        new_weather_events.append(event)
        new_seen_ids.add(event_id)

print(f"Total events fetched: {len(events)}")
print(f"New weather events found: {len(new_weather_events)}")
print()

for event in new_weather_events:
    print("=" * 80)
    print("ID:", event.get("id"))
    print("TITLE:", event.get("title"))
    print("SLUG:", event.get("slug"))
    print("CREATED:", event.get("createdAt"))
    print()

with open(SEEN_FILE, "w") as f:
    json.dump(sorted(list(new_seen_ids)), f, indent=2)

print("Done")
