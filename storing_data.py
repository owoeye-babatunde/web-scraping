# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 13:16:08 2021

@author: user
"""

import os
from urllib.request import urlopen, urlretrieve
from bs4 import BeautifulSoup

downloadDirectory = 'Downloads'
baseUrl = 'http://pythonscraping.com'

def getAbsoluteUrl(baseUrl, source):
    if source.startswith('http://www.'):
        url = 'http://{}'.format(source[11:])
    elif source.startswith('www.'):
        url = 'http://{}'.format(source[4:])
    elif source.startswith('http://'):
        url = source
    else:
        url = '{}/{}'.format(baseUrl, source)
    if baseUrl not in url:
        return None
    return url

def getDownloadPath(baseUrl, absoluteUrl, downloadDirectory):
        path = absoluteUrl.replace('www.', '')
        path = path.replace(baseUrl, '')
        path = downloadDirectory+path
        directory = os.path.dirname(path)
        
        if not os.path.exists(directory):
            os.makedirs(directory)
        return path

html = urlopen('http://www.pythonscraping.com')
bs = BeautifulSoup(html, 'html.parser')
downloadList = bs.find_all(src=True)

for download in downloadList:
    fileUrl = getAbsoluteUrl(baseUrl, download['src'])
    if fileUrl is not None:
        print(fileUrl)
urlretrieve(fileUrl, getDownloadPath(baseUrl, fileUrl, downloadDirectory))
    