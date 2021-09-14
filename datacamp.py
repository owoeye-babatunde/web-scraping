# -*- coding: utf-8 -*-
"""
Created on Thu Aug 19 11:02:29 2021

@author: user
"""

import scrapy
from scrapy.crawler import CrawlerProcess

# Actual spider
class SpiderClassName(scrapy.Spider):
    name = 'dc_spider'
    
    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse)
            
    def parse(self, response):
        #simple example: write out the html
        html_file = 'DC_courses.html'
        with open(html_file, 'wb') as fout:
            fout.write(response.body)
    #the code for your spider
    
   #Running spider 
process = CrawlerProcess()
process.crawl(SpiderClassName)
process.start()
#https://stackoverflow.com/questions/41495052/scrapy-reactor-not-restartable