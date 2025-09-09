import requests

# API endpoint
url = "http://127.0.0.1:5000/items/3"   # Delete item with id=2

# Send DELETE request
response = requests.delete(url)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
