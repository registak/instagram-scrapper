# -*- coding: utf-8 -*-

import scrapy


class InstagramItem(scrapy.Item):
    image_urls = scrapy.Field()
    images = scrapy.Field()
    pass
