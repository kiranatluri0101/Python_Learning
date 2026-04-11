import re

with open('url.txt' , 'r') as file:
  for i in file:
    print(i.split('.')[1])