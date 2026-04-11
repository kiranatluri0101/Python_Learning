import re

pattern="Hello"

#This is to read file content using open
with open('input.txt', 'r') as hello:
    for line in hello:
#This will print the line which contains hello word in input.txt file
       if re.search(pattern, line, re.I):
           print(line.strip())
