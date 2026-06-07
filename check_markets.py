import requests

print("SCRIPT STARTED")

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(
    url,
    params={"limit": 100},
    timeout=30
)

print("STATUS:", response.status_code)

data = response.json()

print("MARKETS:", len(data))

found = 0

keywords = [
    "temperature",
    "weather",
    "rain",
    "snow",
    "nyc",
    "chicago"
]

for market in data:
    question = market.get("question", "").lower()

    for keyword in keywords:
        if keyword in question:
            found += 1
            print(market["question"])
            break

print("FOUND:", found)
