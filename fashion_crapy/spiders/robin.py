# -*- coding: utf-8 -*-
import scrapy
import re
import json
import yaml
from ..items import FashionCrapyItem


class RobinSpider(scrapy.Spider):
    name = 'robin'
    # sitemap_urls = ['https://www.robins.vn/product-sitemap-2.xml']
    start_urls = ["https://www.robins.vn/neo-bag-tui-hop-day-xich-dinh-nhu-thoi-trang-n%C3%A2u-821143.html"]

    def parse(self, response):
        data = re.findall("dataLayer =(.+?);\n", response.body, re.S)
        data_json = yaml.safe_load(data[0])
        images = response.xpath("//*[contains(@class, 'prd-imageBoxLayout ui-border')]//img/@src")
        image_urls = images.extract()
        x = image_urls[0]  # .split("(ffffff)/")[1]
        yield FashionCrapyItem(
            product_name=data_json[0]['Product_Name'],
            gender_cat=data_json[0]['Gender_Category'],
            product_cat=data_json[0]['Product_Category'],
            product_subcat=data_json[0]['Product_Subcategory'],
            brand=data_json[0]['Brand'],
            brand_cat=data_json[0]['Brand_Category'],
            product_price=data_json[0]['Product_Price'],
            file_urls=[x]
        )
