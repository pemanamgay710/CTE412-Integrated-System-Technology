import requests

# API endpoint
url = "http://127.0.0.1:5000/items/1" 

# Data to update
data = {
    "name": "Green Apple",
    "price": 1.5
}

# Send PUT request
response = requests.put(url, json=data)

print("Status Code:", response.status_code)
print("Response JSON:", response.json())
