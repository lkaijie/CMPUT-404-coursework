import requests

# print version of requests

print(requests.__version__) # git test




# getting the google homepage
response = requests.get("http://www.google.com/")
print(response.status_code)

response = requests.get("https://raw.githubusercontent.com/lkaijie/CMPUT-404-coursework/main/lab1/lab1.py")

print(response.status_code)
print(response.text)
