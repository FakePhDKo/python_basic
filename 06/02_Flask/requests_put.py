import requests

# PUT method
url = 'https://jsonplaceholder.typicode.com/users'
data = {"name" : "John", "email" : "john@example.com"}

resp = requests.post(url, json=data)
print(resp.headers)
print(resp.text)