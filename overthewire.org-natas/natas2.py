#!/usr/bin/env python3
import requests 
import re

username = "natas2"
password = 'h4ubbcXrWqsTo7GGnnUMLppXbOogfBZ7'

s = requests.session()

url = 'http://%s.natas.labs.overthewire.org/files/users.txt' % username

r = s.get(url, auth = (username, password))
content = r.text
# print(content)
print(re.findall('natas3:(.*)',content)[0])