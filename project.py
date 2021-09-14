# -*- coding: utf-8 -*-
"""
Created on Sun Jul 25 03:40:47 2021

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jul 21 11:11:12 2021

@author: user
"""

from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen('http://pythonscraping.com/pages/warandpeace.html')
bs = BeautifulSoup(html.read(), 'html.parser')
bs.div 

from urllib.request import urlopen
from urllib.error import HTTPError, URLError
from bs4 import BeautifulSoup
import re
"""
defining a function getTitle which returns either the title of the page, or a 
None object if there was a problem retrieving it.
"""

def getWhatever(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bs = BeautifulSoup(html.read(), 'html.parser')
        title = bs.find_all('img', 
                       {'src':re.compile('..\/img\/gifts/img.*.jpg')}) 
    except AttributeError & URLError() as e:
        return None
    return title
#'http://pythonscraping.com/pages/page1.html'
title = getWhatever('http://pythonscraping.com/pages/page3.html')
if title == None:
    print('Title could not be found')
else:
    print(title)




'''html = urlopen('http://pythonscraping.com/pages/page1.html')
bs = BeautifulSoup(html.read(), 'html.parser')
nameList = bs.find_all('img', 
                       {'src':re.compile('..\/img\/gifts/img.*.jpg')}) 
for name in nameList:
    print(name.get_text())
nameList = bs.find_all(text='the prince')
print(len(nameList))
print(bs.find_all({'id':'span'}))'''
