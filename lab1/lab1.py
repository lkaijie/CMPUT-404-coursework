import requests

# print version of requests

print(requests.__version__)

response = requests.get("https://github.com/lkaijie/CMPUT-404-coursework")

print(response.status_code)
print(response.text)