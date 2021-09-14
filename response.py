# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 07:32:25 2021

@author: user
"""

from scrapy import Selector
import requests
import lxml

url = "https://www.datacamp.com/courses/all"
html = requests.get(url).content
sel = Selector(text = html)
print(response.url)