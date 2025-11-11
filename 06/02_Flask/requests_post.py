import requests

# POST method
url = 'https://jsonplaceholder.typicode.com/users'
data = {"name" : "John", "email" : "john@example.com"}

resp = requests.post(url, json=data)
print(resp.text)
print(resp.status_code)
print(resp.json())