# -*- coding: utf-8 -*-
"""
Created on Wed Aug 18 07:42:27 2021

@author: user
"""

import requests
from bs4 import BeautifulSoup
from lxml import etree

url = "https://en.wikipedia.org/wiki/Nike,_Inc."
headers = ({'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36'})
webpage = requests.get(url, headers=headers)
soup = BeautifulSoup(webpage.content, "html.parser")
dom = etree.HTML(str(soup))
print(dom.xpath('//*[@id="firstHeading"]')[0].text)
