import requests

print(requests.__version__)
response = requests.get("http://google.com")
print(response.text)

response = requests.get("https://raw.githubusercontent.com/AidanHoremans/cmput404Lab1/main/lab1.py")
print(response.text)

open("(1)lab1.py", 'w').write(response.text)
