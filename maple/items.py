# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MapleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
	region = scrapy.Field()
	name = scrapy.Field()
	address = scrapy.Field()
	phone = scrapy.Field()
	web = scrapy.Field()
	email = scrapy.Field()
    pass
