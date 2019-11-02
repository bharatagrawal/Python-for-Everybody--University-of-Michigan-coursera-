# -*- coding: utf-8 -*-
"""
Created on Fri Nov  1 20:41:33 2019

@author: bharatagrawal
"""

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser').text

# Retrieve all of the anchor tags
tags = soup('span')
sum=0
for tag in tags:
    # Look at the parts of a tag
    t= int(tag.text)
    sum =sum+t
print(sum)
