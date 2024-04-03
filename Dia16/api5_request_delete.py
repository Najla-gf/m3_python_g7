import requests

url = "https://jsonplaceholder.typicode.com/posts/10"

payload = {}
headers = {}

response = requests.request("DELETE", url, headers=headers, data=payload)

print(response.text)
