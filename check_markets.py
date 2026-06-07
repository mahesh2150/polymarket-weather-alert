import requests

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(
    url,
    params={"limit": 100},
    timeout=30
)

data = response.json()

keywords = [
    "temperature",
    "weather",
    "rain",
    "snow",
    "nyc",
    "chicago",
    "seattle",
    "high temperature"
]

for market in data:
    question = market.get("question", "").lower()

    for keyword in keywords:
        if keyword in question:
            print("=" * 60)
            print("ID:", market["id"])
            print("QUESTION:", market["question"])
            break
