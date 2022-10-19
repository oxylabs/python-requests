import requests

response = requests.get('http://httpbin.org/')

print(response.status_code)
print(response.text)