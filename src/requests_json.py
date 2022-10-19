import json
import requests

payload = {
    'key1': 'value1',
    'key2': 'value2'}
jsonData = json.dumps(payload)
response = requests.post('https://httpbin.org/post', data = jsonData)
print(response.json())
