# -*- coding: utf-8 -*-
"""
Created on Sat Aug 14 04:21:08 2021

@author: user
"""

from bs4 import BeautifulSoup
import csv
import requests

html = requests.get('https://docs.google.com/spreadsheets/d/e/2PACX-1vSc_2y5N0I67wDU38DjDh35IZSIS30rQf7_NYZhtYYGU1jJYT6_kDx4YpF-qw0LSlGsBYP8pqM_a1Pd/pubhtml').text
soup = BeautifulSoup(html, "lxml")
tables = soup.find_all("table")
index = 0
for table in tables:
    with open(str(index) + ".csv", "w", encoding='utf-8') as f:
        wr = csv.writer(f, quoting=csv.QUOTE_NONNUMERIC)
        wr.writerows([[td.text for td in row.find_all("td")] for row in table.find_all("tr")])
    index = index + 1