import requests

# script de check de code html
print("Check html code for google.com"
)

url = "https://www.google.com"
response = requests.get(url)

print("Code retour HTTP :", response.status_code)