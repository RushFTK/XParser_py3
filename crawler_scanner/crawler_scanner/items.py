# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#找到的输入点对象，也可能是包含在表单中
class CrawledInputs(scrapy.Item):
    source_url = scrapy.Field()
    id = scrapy.Field()
    name = scrapy.Field()
    style_class = scrapy.Field()
    type = scrapy.Field()
    value = scrapy.Field()

# 找到的表单对象
class CrawledForm(scrapy.Item):
    request_method = scrapy.Field()    #判断是GETS还是POST型表单
    action = scrapy.Field()
    inputs = scrapy.Field()            #表单中可提交的项
    pass
