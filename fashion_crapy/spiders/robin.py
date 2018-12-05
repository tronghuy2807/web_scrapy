# -*- coding: utf-8 -*-
import scrapy
from scrapy.spiders import SitemapSpider
import re
import json
import yaml
from ..items import FashionCrapyItem


class RobinSpider(SitemapSpider):
    name = 'robin'
    sitemap_urls = ['https://www.robins.vn/product-sitemap-2.xml']

    def parse(self, response):
        data = re.findall("dataLayer =(.+?);\n", response.body, re.S)
        data_json = yaml.safe_load(data[0])
        url = response.url
        colors = response.xpath("//*[contains(@id, 'productDetails')]//table//tr[2]//td[2]//text()").extract()
        color = colors[0].strip()
        images = response.xpath("//*[contains(@class, 'prd-imageBoxLayout ui-border')]//img/@src")
        image_urls = images.extract()
        image_url = image_urls[0]
        yield FashionCrapyItem(
            product_name=data_json[0]['Product_Name'],
            gender_cat=data_json[0]['Gender_Category'],
            product_cat=data_json[0]['Product_Category'],
            product_subcat=data_json[0]['Product_Subcategory'],
            brand=data_json[0]['Brand'],
            brand_cat=data_json[0]['Brand_Category'],
            product_price=data_json[0]['Product_Price'],
            discount=data_json[0]['Discount_%'],
            color=color,
            product_url=url,
            file_urls=[image_url]
        )
