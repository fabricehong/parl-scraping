# -*- coding: utf-8 -*-
"""
Hackaton Le Temps 2015

Spiders - Basic v2

Takes 1 list of url in input and outputs a json file in /data
NB inbound URLs must be Subject url within a Séance.
"""
__author__ = """Giovanni Colavizza"""

import scrapy, codecs, requests
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from hackaton.items import HackatonItem
from hackaton.text_cleaning import clean_format

base_link = "http://www.parlament.ch"
allowed_base = "/ab/frameset/f/n/"

# getting urls to parse from txt file
input_file = "debates-urls.txt"
urls = codecs.open(input_file, "rb", "utf-8").read()
start_urls = list()
for line in urls.split("\n"):
    line = line[1:-1]
    if allowed_base not in line:
        continue
    url = base_link+"/"+line
    #r = requests.get(url)
    #if r.status_code == requests.codes.ok:
    start_urls.append(url)
    print(url)

class ConseilNationalSpider(CrawlSpider):
    name = "CNbasic2"
    allowed_domains = ["parlament.ch"]
    start_urls = start_urls
    """
    start_urls = [
        "http://www.parlament.ch/ab/frameset/f/n/4918/463775/f_n_4918_463775_463870.htm",
        "http://www.parlament.ch/ab/frameset/f/n/4918/463775/f_n_4918_463775_463783.htm",
        "http://www.parlament.ch/ab/frameset/f/n/4918/463775/f_n_4918_463775_463934.htm",
        "http://www.parlament.ch/ab/frameset/f/n/4918/463775/f_n_4918_463775_463882.htm",
        "http://www.parlament.ch/ab/frameset/f/n/4918/463775/f_n_4918_463775_463906.htm"
    ]
    """

    rules = [
        Rule(LinkExtractor(tags=('a', 'area', 'frame'), attrs=('href','src')), callback='parse')
    ]

    def parse(self, response):
        links = list()
        for link in response.xpath("//a/@href").extract():
            link = base_link + link
            links.append(link)
        for link in response.xpath("//frame[@name=\"main\"]/@src").extract():
            link = base_link + link
            links.append(link)
        for link in links:
            yield scrapy.Request(link, callback=self.parse_item, meta={'link':link})


    def parse_item(self, response):

        for sel in response.xpath('//pd_text'):
            item = HackatonItem()

            # Subject id and date
            title = response.xpath('//title/text()').extract()[0].split("-")
            item['id_subject'] = title[0].strip()
            item['date'] = title[-2].strip()
            # Séance title
            item['session_title'] = response.xpath('//tr[@id="SessionTitleLine"]/descendant::*/text()').extract()[1]
            # Project description
            item['description'] = response.xpath('//meta[@name="description"]/@content').extract()[0]
            # Link to subject page
            item['link_subject'] = response.xpath('//a[*/span/text() = "Informations CuriaVista"]/@href').extract()[0]
            # Surname and infos of the person speaking
            item['surname'] = sel.xpath('span/b/a[@target=\"_blank\"]/text()').extract()
            name = sel.xpath('span/text()').extract()
            if len(name) < 1:
                continue
            else:
                name = name[0]
                item['surname'] = item['surname'][0]
            item['name'] = name.split()[0].strip()
            item['name'] = item['name'].replace(",", "")
            item['role'] = ""
            if len(name.split(",")) == 3:
                item['role'] = name.split(",")[-1].strip()
                item['role'] = item['role'].replace(":", "")
            item['group'] = ""
            item['canton'] = ""
            if len(name.split("(")) > 1:
                name = name.split("(")[1]
                name = name.split(")")[0]
                item['group'] = name.split(",")[0].strip()
                item['canton'] = name.split(",")[1].strip()
                item['canton'] = item['canton'].replace(")","")
            # Link to the page of the person speaking
            item['bio'] = sel.xpath('span/b/a[@target=\"_blank\"]/@href').extract()
            if len(item['bio']) < 1:
                continue
            else:
                item['bio'] = item['bio'][0]
            # Text of intervention
            #item['data'] = " ".join(sel.xpath('descendant::*/text()').extract())#.encode("utf-8")
            item['data'] = clean_format(" ".join(sel.xpath('descendant-or-self::*/text()').extract()).encode("utf-8"))
            item['data'] = "".join(item['data'].split(":")[1:]).strip()
            #item['data'] = sel.xpath('descendant-or-self::*/text()').extract()
            yield item