# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class HackatonItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    id_subject = scrapy.Field()
    date = scrapy.Field()
    session_title = scrapy.Field()
    description = scrapy.Field()
    link_subject = scrapy.Field()
    name = scrapy.Field()
    surname = scrapy.Field()
    role = scrapy.Field()
    canton = scrapy.Field()
    group = scrapy.Field()
    bio = scrapy.Field()
    data = scrapy.Field()
