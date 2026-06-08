import requests
import json
import os
from datetime import datetime, timedelta

BOT_TOKEN = os.environ.get("BOT_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

SEEN_FILE = "seen_events.json"
URL = "https://gamma-api.polymarket.com/events/keyset"

try:
    # Fetch events
    response = requests.get(
        URL,
        params={
            "limit": 300,
            "tag_slug": "weather",
            "closed": "false",
            "order": "createdAt",
            "ascending": "false"
        },
        timeout=30
    )

    response.raise_for_status()

    data = response.json()
    events = data.get("events", [])

    print(f"Weather events found: {len(events)}")

    # Load seen IDs
    try:
        if os.path.exists(SEEN_FILE):
            with open(SEEN_FILE, "r") as f:
                seen_ids = set(json.load(f))
        else:
            seen_ids = set()

    except Exception as e:
        print("Error loading seen_events.json:", str(e))
        seen_ids = set()

    new_ids = set(seen_ids)
    new_events = []

    for event in events:

        title = event.get("title", "").lower()
        slug = event.get("slug", "").lower()

        if (
            "highest temperature" not in title
            and "highest-temperature" not in slug
        ):
            continue

        event_id = str(event.get("id"))

        if event_id not in seen_ids:
            new_events.append(event)
            new_ids.add(event_id)

    print(f"New events found: {len(new_events)}")

    # Skip alert storm on first run
    if len(seen_ids) == 0:
        print("First run detected. Seeding IDs only.")

    else:

        for event in new_events:

            try:

                title = event.get("title", "Unknown Market")
                slug = event.get("slug", "")
                created_at = event.get("createdAt", "")

                try:
                    dt = datetime.fromisoformat(
                        created_at.replace("Z", "+00:00")
                    )

                    ist_time = dt + timedelta(hours=5, minutes=30)

                    created_display = ist_time.strftime(
                        "%d-%b-%Y %I:%M:%S %p IST"
                    )

                except Exception:
                    created_display = created_at

                message = (
                    f"🚨 New Temperature Market\n\n"
                    f"📌 {title}\n\n"
                    f"🕒 Created: {created_display}\n\n"
                    f"🔗 https://polymarket.com/event/{slug}"
                )

                telegram_response = requests.post(
                    f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
                    data={
                        "chat_id": CHAT_ID,
                        "text": message
                    },
                    timeout=30
                )

                print(
                    "Telegram response:",
                    telegram_response.status_code,
                    telegram_response.text
                )

                print("Alert sent:", title)

            except Exception as e:
                print(
                    f"Error sending alert for '{title}':",
                    str(e)
                )

    # Save IDs
    try:
        with open(SEEN_FILE, "w") as f:
            json.dump(sorted(list(new_ids)), f, indent=2)

    except Exception as e:
        print("Error saving seen_events.json:", str(e))

except Exception as e:
    print("FATAL ERROR:", str(e))
