# -*- coding: utf-8 -*-
import scrapy
#from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.contrib.linkextractors import LinkExtractor
from scrapy.item import Item, Field

class MyItem(Item):
    url= Field()

class RobinSpider(scrapy.Spider):
    name = 'robin'

    def start_requests(self):
        url = "https://www.robins.vn/92wear-dam-so-mi-beo-duoi-ca-3-tang-xanh-d%C6%B0%C6%A1ng-832227.html/"
        yield scrapy.Request(url, self.parse)

    def parse(self, response):
        item = MyItem()
        item['url'] = []
        for image in response.xpath('//img/@src').extract():
            item['url'].append(response.urljoin(image))
            print item
