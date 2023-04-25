import requests


print('Hello World')

url = 'https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v2.0/json/petstore-simple.json'
r = requests.get(url)

print(r.json())