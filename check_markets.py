import requests

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(
    url,
    params={"limit": 500},
    timeout=30
)

data = response.json()

found = 0

for market in data:
    slug = market.get("slug", "").lower()
    question = market.get("question", "").lower()

    if "temperature" in slug or "temperature" in question:
        found += 1
        print("=" * 60)
        print("ID:", market.get("id"))
        print("QUESTION:", market.get("question"))
        print("SLUG:", market.get("slug"))

print("\nFOUND:", found)
