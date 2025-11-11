import requests

# GET method
url = 'https://jsonplaceholder.typicode.com/users'
resp = requests.get(url)
print(resp.text)
print(resp.status_code)
print(resp.json())