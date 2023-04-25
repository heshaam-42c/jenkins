import json
import requests

#url = 'https://raw.githubusercontent.com/OAI/OpenAPI-Specification/main/examples/v2.0/json/petstore-simple.json'
url = 'https://raw.githubusercontent.com/heshaam-42c/platform-demo/main/OASFiles/PixiVersions/Pixiv4_RemediatedVersion_3.0_hesh.json?token=GHSAT0AAAAAAB5FCRJMDWRKHAQ456ECHCP4ZCIAWRQ'
r = requests.get(url)

print('Fetching pixi-v3.0 from URL: https://raw.githubusercontent.com/heshaam-42c/platform-demo/main/OASFiles/PixiVersions/Pixiv4_RemediatedVersion_3.0_hesh.json?token=GHSAT0AAAAAAB5FCRJMDWRKHAQ456ECHCP4ZCIAWRQ \n')
print(r.json())

datastr = json.dumps(r.json())

oasFile = 'OASFiles/pixi-v3.0.json'

# Write to file
f = open(oasFile,'w')
f.write(datastr)