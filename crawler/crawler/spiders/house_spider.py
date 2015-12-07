# encoding=utf-8

import scrapy

class HouseSpider(scrapy.Spider):
    '''
    house info spider
    '''

    name = 'hspider'
    allowed_domains = ['58.com']
    start_urls = [
            'http://sh.58.com/chuzu/',
            ]

    def parse(self, response):
        houses = response.xpath('//tr/td[@class="t qj-rentd"]')
        for house in houses:
            titles = house.xpath('a/text()').extract()
            title = titles[0]
            addr= house.xpath('p[@class="qj-renaddr"]/a/text()').extract()
            if len(addr) > 0:
                road = addr[0]
            if len(addr) > 1:
                community = addr[1]
            print title, road, community
