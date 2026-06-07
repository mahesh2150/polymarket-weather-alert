import requests

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(url, timeout=30)

data = response.json()

print("Markets Found:", len(data))
print()

for market in data:
    print("=" * 60)
    print("ID:", market.get("id"))
    print("QUESTION:", market.get("question"))

    if "tags" in market:
        print("TAGS:", market.get("tags"))
