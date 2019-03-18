# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

#爬取范围:http://www.xssed.com/archive/special=1/page=1/
#http://www.xssed.com/archive/special=1/page=491/
#好爬，数据更新不及时。
class xssed_Archive(scrapy.Item):
    id = scrapy.Field() #在XSSed上的条目id，用于识别唯一性
    date_submitted = scrapy.Field() #漏洞提交的时间，用于计算可信度
    vector = scrapy.Field() #含攻击向量的网址要素
    domain = scrapy.Field() #目标网站的域名，用于分离攻击向量
    fixed_state = scrapy.Field() #攻击向量有效性
    pass

#来源：https://www.exploit-db.com/?tag=8
#未知是否能爬，需要文字分析
class exploitdb_archive(scrapy.Item):
    source_url = scrapy.Field() #对攻击向量说明的源链接
    description = scrapy.Field() #对于漏洞描述的文字性说明
    verified =  scrapy.Field()


