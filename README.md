# Python Requests Library

[![Oxylabs promo code](https://user-images.githubusercontent.com/129506779/250792357-8289e25e-9c36-4dc0-a5e2-2706db797bb5.png)](https://oxylabs.go2cloud.org/aff_c?offer_id=7&aff_id=877&url_id=112)

[![](https://dcbadge.vercel.app/api/server/eWsVUJrnG5)](https://discord.gg/GbxmdGhZjq)

[<img src="https://img.shields.io/static/v1?label=&message=Requets&color=brightgreen" />](https://github.com/topics/requests) [<img src="https://img.shields.io/static/v1?label=&message=Python&color=important" />](https://github.com/topics/python)

- [Getting started with Requests](#getting-started-with-requests)
- [Python requests: GET](#python-requests-get)
- [Reading responses](#reading-responses)
- [Using Python request headers](#using-python-request-headers)
- [Python requests: POST](#python-requests-post)

The **Requests** module is one widely used to send HTTP requests. It’s a third-party alternative to the standard [urllib](https://docs.python.org/3/library/urllib.html), [urllib2](https://docs.python.org/2/library/urllib2.html), and [urllib3](https://urllib3.readthedocs.io/en/latest/) as they can be confusing and often need to be used together. **Requests** in Python greatly simplifies sending HTTP requests to their destination.

This article gives you an overview of everything you need about Requests.

For a detailed explanation, see our [blog post](https://oxylabs.io/blog/python-requests).

## Getting started with Requests

Installing Requests is simple as it can be done through a terminal.  

```shell
$ pip install requests
```

Finally, before beginning to use Requests in any project, the library needs to be imported:

```python
import requests
```

## Python requests: GET

To send a GET request, invoke `requests.get()` in Python and add a destination URL, as follows:  

```python
import requests
requests.get('http://httpbin.org/')
```

GET requests can be sent with specific parameters if required:  

```python
payload = {'key1': 'value1', 'key2': 'value2'}
requests.get('http://httpbin.org/', params=payload)
```

## Reading responses

```python
response = requests.get('http://httpbin.org/')
print(response.status_code)

# OUTPUT: <Response [200]>
```

To read the content of the response, we need to access the text part by using `response.text`:  

```python
print(response.text)
```

Responses can also be decoded to the JSON format:

```python
response = requests.get('http://api.github.com')
print(response.json())
```

## Using Python request headers

Response headers are another important part of the request:  

```python
print(response.headers)
```

You can also send custom Python request headers. To check whether our request header has been sent successfully, we will need to make the call `response.request.headers`:  

```python
import requests

headers = {'user-agent': 'my-agent/1.0.1'}
response = requests.get('http://httpbin.org/', headers=headers)
print(response.request.headers)
```

## Python requests: POST

Sending a POST request is *almost* as simple as sending a GET:  

```python
response = requests.post('https://httpbin.org/post', data = {'key':'value'})
```

The requests library accepts arguments from dictionary objects which can be utilized to send more advanced data:

```python
payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data = payload)
```

Requests have an added feature that automatically converts the POST request data into JSON.

```python
import requests

payload = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', json = payload)
print(response.json())
```

Alternatively, the *json* library might be used to convert dictionaries into JSON objects:

```python
import json
import requests

payload = {
    'key1': 'value1',
    'key2': 'value2'}
jsonData = json.dumps(payload)
response = requests.post('https://httpbin.org/post', data = jsonData)
print(response.json())
```

If you wish to learn more about Requests, see our [blog post](https://oxylabs.io/blog/python-requests).
