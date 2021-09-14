# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 07:41:31 2021

@author: user
"""


from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

html = urlopen('http://pythonscraping.com/pages/page3.html')
bs = BeautifulSoup(html, 'html.parser')
images = bs.find_all('img', 
                     {'src': re.compile('..\/img\/gifts/img.*.jpg')})
for image in images:
    print(image['src'])
#print(bs.find_all('img'.attrs['src']))
print(bs.find_all(lambda img: len(img.attrs)==2))
print()
print()
print(bs.find_all(lambda img: img.get_text() == 'Or maybe he\'s only resting?'))
print(bs.find_all('', text ='Or maybe he\'s only resting?'))
