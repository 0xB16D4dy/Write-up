#!/usr/bin/env python3
import requests 
import re

username = "natas1"
password = 'g9D9cREhslqBKtcA2uocGHPfMZVzeFK6'

s = requests.session()

url = 'http://%s.natas.labs.overthewire.org' % username
r = s.get(url, auth = (username, password))
content = r.text
# print(content)
print(re.findall('<!--The password for natas2 is (.*) -->',content)[0])