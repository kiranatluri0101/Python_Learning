import requests

url = "https://www.google.com/"
response = requests.get(url)
print(response)

if response.status_code == 200:
    print("Success! URL returned 200 OK.")
else:
    print(f"Failed with status code: {response.status_code}")
