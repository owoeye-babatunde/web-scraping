# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 02:16:48 2021

@author: user
"""

from bs4 import BeautifulSoup
import scrapy
from urllib.request import urlopen

html = urlopen('https://www.icloud.com/')
bs = BeautifulSoup(html, 'html.parser')
print(bs)