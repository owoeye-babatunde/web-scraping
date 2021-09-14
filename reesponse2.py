# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 08:00:43 2021

@author: user
"""
from scrapy import Selector
import requests
from lxml import etree

url = "https://www.datacamp.com/courses/all"
response = requests.get(url).content
sel = Selector(text = response)
print(response.xpath('//div/span[@class="bio"]'))
