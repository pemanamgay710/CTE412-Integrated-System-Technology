import requests

# API endpoint
url = "http://127.0.0.1:5000/items"

# Data to add
data = {
    "name": "Mango",
    "price": 400,

}

# Send POST request
response = requests.post(url, json=data)

# Print response from API
print("Status Code:", response.status_code)
print("Response JSON:", response.json())
