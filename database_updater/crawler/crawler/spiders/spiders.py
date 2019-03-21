from urllib import parse
from ..items import xssed_Archive
import scrapy

# 获取详细页面的列表
# 爬取范围:http://www.xssed.com/archive/special=1/page=1/
# http://www.xssed.com/archive/special=1/page=491/
class xssed_index_spider(scrapy.Spider):
    name = "xssed_index_spider"
    allowed_domains = ['www.xssed.com']
    # start_urls = ['http://www.xssed.com/archive/special=1/page=1/']
    #使用这个站点获取数量更高但质量不高的XSS信息
    #start_urls = ['http://www.xssed.com/archive']
    start_urls = ['http://www.xssed.com/archive/page=917/']
    def parse(self, response):
        full_url_list = []  #存储获得的所有有效mirror的列表
        #检索目录页，获取每一个mirrors的间接地址
        for eachline in response.xpath( '//*[@id="tableborder"]/table/tr'):
            mirrors_type = eachline.xpath('th[8]/text()').extract()[0]
            if (mirrors_type == 'XSS'):
                mirrors_url = eachline.xpath('th[9]/a/@href').extract()
                if(len(mirrors_url) > 0):
                    full_url_list.append(parse.urljoin(response.url,mirrors_url[0]))
        #本页扒取完毕，判断页尾跳转导航是否在对应位置存在">"，如果存在，则跳转下一页。
        next_page_linker = response.xpath('//*[@id="contentpaneOpen"]/table/div/a[last()-2]')
        if (len(next_page_linker.xpath('text()').extract()) > 0):
            symbol = next_page_linker.xpath('text()').extract()[0]
            print('symbol:' + symbol )
            if (symbol == '>'):
                next_page_link = parse.urljoin(response.url, next_page_linker.xpath('@href').extract()[0])
                yield scrapy.Request(next_page_link , callback=self.parse)
        #对获取到的进行处理，第一行为存储列表文件，第二行为爬mirrors页面的内容
        #self.save_urllist_file(full_url_list)
        for urls in full_url_list:
            yield scrapy.Request(urls,callback=self.parse_mirrors)

    #对抓取到的特定页面进行爬取
    def parse_mirrors(self, response):
        id = response.url.split('/')[4]
        #在Chrome浏览器中提取出的位置//*[@id="contentpaneOpen"]/table/tbody/tr[2]/th[1]
        Date_submitted = response.xpath('//*[@id="contentpaneOpen"]/table/div[2]/tr/th[1]/text()').extract()[0].split('Date submitted:\xa0')[1]
        # // *[ @ id = "contentpaneOpen"] / table / tbody / tr[4] / th
        vector = response.xpath('//*[@id="contentpaneOpen"]/table/div[4]/tr/th/text()').extract()[0].split('URL: ')[1]
        # // *[ @ id = "contentpaneOpen"] / table / tbody / tr[3] / th[2]
        domain = response.xpath('//*[@id="contentpaneOpen"]/table/div[3]/tr/th[2]/text()').extract()[0].split('Domain: ')[1]
        # //*[@id="contentpaneOpen"]/table/tbody/tr[2]/th[4]
        fixed_state = response.xpath('//*[@id="contentpaneOpen"]/table/div[2]/tr/th[4]/text()').extract()[1].split('\xa0')[1]
        # 封装到items中
        current_item = xssed_Archive()
        current_item['id']=id
        current_item['date_submitted'] = Date_submitted
        current_item['vector'] = vector
        current_item['domain'] = domain
        current_item['fixed_state'] = fixed_state
        #对获取到的进行处理
        #TODO:整合到pipelines，使用json存储
        full_items = [ current_item['id'],current_item['date_submitted'],current_item['vector'],current_item['domain'],current_item['fixed_state']]
        spliter = '|' #分割存储的元素
        with open('xssed_mirrors_list.csv', 'a') as f:
            for items in full_items:
                f.write(items + spliter)
            f.write('\n')
            f.close()

    def save_urllist_file(self, full_url_list):
        with open('xssed_mirrors_url_list.txt', 'a') as f:
            for urls in full_url_list:
                f.write(urls + '\n')
            f.close()

#单独扒取xssed中一条记录信息的爬虫(Abroted)
class xssed_mirrors_spider(scrapy.Spider):
    name = "xssed_mirrors_spider"
    allowed_domains = ['www.xssed.com']
    start_urls = ['http://www.xssed.com/mirror/81282/']

    def parse(self, response):
        #在Chrome浏览器中提取出的位置//*[@id="contentpaneOpen"]/table/tbody/tr[2]/th[1]
        Date_submitted = response.xpath('//*[@id="contentpaneOpen"]/table/div[2]/tr/th[1]/text()').extract()[0].split('Date submitted:\xa0')[1]
        # // *[ @ id = "contentpaneOpen"] / table / tbody / tr[4] / th
        vector = response.xpath('//*[@id="contentpaneOpen"]/table/div[4]/tr/th/text()').extract()[0].split('URL: ')[1]
        # // *[ @ id = "contentpaneOpen"] / table / tbody / tr[3] / th[2]
        domain = response.xpath('//*[@id="contentpaneOpen"]/table/div[3]/tr/th[2]/text()').extract()[0].split('Domain: ')[1]
        # //*[@id="contentpaneOpen"]/table/tbody/tr[2]/th[4]
        fixed_state = response.xpath('//*[@id="contentpaneOpen"]/table/div[2]/tr/th[4]/text()').extract()[1].split('\xa0')[1]
        # 封装到items中
        current_item = xssed_Archive()
        current_item['date_submitted'] = Date_submitted
        current_item['vector'] = vector
        current_item['domain'] = domain
        current_item['fixed_state'] = fixed_state
        #对获取到的进行处理
        #TODO:整合到pipelines
        full_items = [current_item['date_submitted'],current_item['vector'],current_item['domain'],current_item['fixed_state']]
        #with open('xssed_mirrors_list.csv', 'a') as f:
        #    for items in full_items:
        #        f.write(items + ',')
        #    f.write('\n')
        #    f.close()
        return current_item

class owsap_XSSFilterEvasionCheatSheet(scrapy.Spider):
    name = "OWSAP_XSSFilterEvasionCheatSheet_spider"
    allowed_domains = ['www.owasp.org']
    start_url = 'https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet#Basic_XSS_Test_Without_Filter_Evasion'

    def parse(self, response):
        # 所有Sheet的样例均存在<pre>标签中
        pass
