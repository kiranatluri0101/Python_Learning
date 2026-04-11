import requests
#url = "https://www.google.com/"
with open('url.txt' , 'r') as file:
  for url in file:
    platform = url.split('.')[1]
    response = requests.get(url)
    print(platform,  response)
#print(response)