import requests
import json
import os

BOT_TOKEN = os.environ["BOT_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

SEEN_FILE = "seen_events.json"

URL = "https://gamma-api.polymarket.com/events/keyset"

response = requests.get(
    URL,
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

# Load seen IDs
if os.path.exists(SEEN_FILE):
    with open(SEEN_FILE, "r") as f:
        seen_ids = set(json.load(f))
else:
    seen_ids = set()

new_ids = set(seen_ids)

new_events = []

for event in events:
    event_id = str(event["id"])

    if event_id not in seen_ids:
        new_events.append(event)
        new_ids.add(event_id)

print(f"Weather events found: {len(events)}")
print(f"New events found: {len(new_events)}")

# Skip alert storm on first run
if len(seen_ids) == 0:
    print("First run detected. Seeding IDs only.")

else:
    for event in new_events:

        title = event["title"]
        slug = event["slug"]

        message = (
            f"🚨 New Weather Market\n\n"
            f"{title}\n\n"
            f"https://polymarket.com/event/{slug}"
        )

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            data={
                "chat_id": CHAT_ID,
                "text": message
            },
            timeout=30
        )

        print("Alert sent:", title)

# Save IDs
with open(SEEN_FILE, "w") as f:
    json.dump(sorted(list(new_ids)), f, indent=2)
