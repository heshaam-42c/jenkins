import json
import requests

url = 'https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v2.0/json/petstore-simple.json'
r = requests.get(url)

print('Fetching petstore-simple.json: \n\n')
print(r.json())

datastr = json.dumps(r.json())

oasFile = 'OASFiles/petstore-simple.json'

# Write to file
f = open(oasFile,'w')
f.write(datastr)