# -*- coding: utf-8 -*-
"""
Hackaton Le Temps 2015

Spiders - Basic
"""
__author__ = """Giovanni Colavizza"""

import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hackaton.items import HackatonItem

class ConseilNationalSpider(CrawlSpider):
    name = "CNbasic"
    allowed_domains = ["parlament.ch"]
    start_urls = [
        "http://www.parlament.ch/ab/toc/f/n/4919/f_n_4919.htm",
        "http://www.parlament.ch/ab/toc/f/n/4919/467616/f_n_4919_467616.htm"
    ]

    rules = [
        Rule(LinkExtractor(tags=('a', 'area', 'frame'), attrs=('href','src')), callback='parse_item')
    ]

    #def parse(self, response):
    #    for href in response.css("a::attr('href')"):
    #        url = response.urljoin(href.extract())
    #        yield scrapy.Request(url, callback=self.parse_dir_contents)

    def parse_item(self, response):
        filename = response.url.split("/")[-2] + response.url.split("/")[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
        for sel in response.xpath('//pd_text'):
            item = HackatonItem()
            #item['title'] = sel.xpath('head/title/text()').extract()
            #item['link'] = sel.xpath('a/@href').extract()
            item['data'] = sel.xpath('text()').extract()
            item['name'] = sel.xpath('a/text()').extract()
            item['bio'] = sel.xpath('a/@href').extract()
            yield item