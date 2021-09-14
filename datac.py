# -*- coding: utf-8 -*-
"""
Created on Sun Sep  5 13:44:49 2021

@author: user
"""

import scrapy
from scrapy.crawler import CrawlerProcess
from twisted.internet import reactor

# Actual spider
class DC_Chapter_Spider(scrapy.Spider):
    name = 'dc_chapter_spider'
    
    def start_requests(self):
        urls = ['https://www.datacamp.com/courses/all']
        for url in urls:
            yield scrapy.Request(url = url, callback = self.parse_front)
            
    def parse_front(self, response):
    ## code to parse the front couses page
        #Narrow in one course block
        course_blocks = response.css('div.course-block')
        ##direct to the course link
        course_links = course_blocks.xpath('./a/@href')
        #Extract the links (as a list of strings)
        links_to_follow = course_links.extract()
        # Follow the links to the next parser
        
        for url in links_to_follow:
            yield response.follow(url = url,
                                  callback = self.parse_pages)
            
    
    
    
    def parse_pages(self, response): 
        # Direct to the course title text
        crs_title = response.xpath('//h1[contains(@class,"title)]/text()')
        # Extract and clean the course title text
        crs_title_ext = crs_title.extract_first().strip()
        # Direct to the chapter titles text
        ch_titles = response.css('h4.chapter__title::text')
        # Extract and clean the chapter title text
        ch_titles_ext = [t.strip() for t in ch_titles.extract()]
        # Store this in our dictionary
        dc_dict[crs_title_ext] = ch_titles_ext
        
        
    ## code to parse course pages
    ## fill in the dc_dict here
    
dc_dict = dict()

process = CrawlerProcess()
process.crawl(DC_Chapter_Spider)
process.start()
#https://stackoverflow.com/questions/41495052/scrapy-reactor-not-restartable