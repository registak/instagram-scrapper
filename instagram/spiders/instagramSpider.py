# -*- coding: utf-8 -*-
import re
import json
from PIL import Image
from urlparse import urlparse
import scrapy

from instagram.items import InstagramItem

class InstagramspiderSpider(scrapy.Spider):
    name = "instagramSpider"
    allowed_domains = ["instagram.com"]

    def start_requests(self):
        url = "https://www.instagram.com/explore/tags/"
        tag = getattr(self, 'tag', None)
        if tag is not None:
            url += tag
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        javascript = "".join(response.xpath('//script[contains(text(), "sharedData")]/text()').extract())
        json_data = json.loads("".join(re.findall(r'window._sharedData = (.*);', javascript)))

        data = get_extracted(json_data["entry_data"]["TagPage"])
        for target in data["tag"]["media"]["nodes"]:
            yield {'image_urls': [target["display_src"]] }

def get_extracted(values, index=0):
    try:
        return values[index]
    except:
        return ""
