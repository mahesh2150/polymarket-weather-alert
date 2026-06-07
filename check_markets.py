import requests

url = "https://gamma-api.polymarket.com/markets"

response = requests.get(url, timeout=30)

print("Status:", response.status_code)

data = response.json()

print("Markets Found:", len(data))

print("\nFIRST MARKET:\n")
print(data[0])
