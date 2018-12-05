# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FashionCrapyItem(scrapy.Item):
    product_name = scrapy.Field()
    gender_cat = scrapy.Field()
    product_cat = scrapy.Field()
    product_subcat = scrapy.Field()
    brand = scrapy.Field()
    brand_cat = scrapy.Field()
    product_price = scrapy.Field()
    discount = scrapy.Field()
    color = scrapy.Field()
    product_url = scrapy.Field()
    file_urls = scrapy.Field()

