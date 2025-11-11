import requests

# PUT method
url = 'https://jsonplaceholder.typicode.com/users/1'
data = {"name" : "John", "email" : "john@example.com"}

resp = requests.delete(url)
print(resp.headers)
print(resp.text)