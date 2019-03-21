import scrapy
import scrapy_splash
import json
import re
from ..items import CrawledInputs,CrawledForm
from scrapy.conf import settings as scrapy_setting_info
from scrapy.exporters import JsonItemExporter
from urllib.parse import urlparse
from urllib.parse import urljoin

class scannerspider(scrapy.Spider):
    name = "scanner_splash"
    url_lists = []
    custom_settings = {
        'DEPTH_LIMIT': 2,
        'DEPTH_PRIORITY': 1,
        'SCHEDULER_DISK_QUEUE' : 'scrapy.squeues.PickleFifoDiskQueue',
        'SCHEDULER_MEMORY_QUEUE' : 'scrapy.squeues.FifoMemoryQueue'
    }

    def __init__(self, start_urls=None, depth=None, no_next_crawl=None, *args, **kwargs):
        super(eval(self.__class__.__name__), self).__init__(*args, **kwargs)
        self.start_url = start_urls
        #仅允许访问目标网址所在站点
        parsed_url = urlparse(start_urls)
        self.allowed_domain = parsed_url.netloc
        if (depth != None):
            self.custom_settings['DEPTH_LIMIT'] = depth
            self.depth = depth
        if (no_next_crawl != None):
            self.no_next_crawl = True
        else:
            self.no_next_crawl = False

    def start_requests(self):
        yield scrapy_splash.SplashRequest(self.start_url, self.parse)

    def parse(self, response):
        next_url_list = []
        form_list = []
        input_list = []
        #获取该网页表单信息
        current_page_form_list,current_page_input_list = self.get_formitem_and_inputitem(response)
        form_list = current_page_form_list
        #存储注入点信息
        with open('injured_form_list.json', 'a') as f:
            for item in current_page_form_list:
                json.dump(dict(item), f)
                f.write('\n')
 #               item_js = json.dumps(dict(item),  indent=4, separators=(',', ':'))
 #               f.write(item_js)
 #               f.write('\n')
        input_list = current_page_input_list
        with open('injured_input_list.json', 'a') as f:
            for item in current_page_input_list:
                json.dump(dict(item),f)
                f.write('\n')
 #               item_js = json.dumps(dict(item), indent=4, separators=(',', ':'))
 #               f.write(item_js)
 #               f.write('\n')
        #print(form_list)
        #print(input_list)

        #获取其他网页链接
        if (not self.no_next_crawl):
            other_page_list = response.xpath('//@href|//@src|//@action')
            for link in other_page_list:
                link_extracted = link.extract()
                if (link_extracted != ''):
                    if ((urlparse(link_extracted).netloc == '') or (
                            urlparse(link_extracted).netloc == self.allowed_domain)):
                        accept_re = r'(\.php)|(\.html)'
                        if ('.' in link_extracted):
                            if (re.search(accept_re, link_extracted) == None):
                                continue
                        accept_url = urljoin(response.url, link.extract())
                        next_url_list.append(accept_url)
            for url in next_url_list:
                yield scrapy_splash.SplashRequest(url, callback=self.parse)
        #    if (urlparse(link).netloc != None):
        #         if (urlparse(link).netloc != self.allowed_domain):  continue
        #     else:
        #         link = urljoin(response.url,link)
        #     next_url_list.append(link)
        # for url in next_url_list:
        #     yield  scrapy_splash.SplashRequest(url,callback=self.parse)




    def get_formitem_and_inputitem(self,response):
        form_list = []
        indivial_input_list = []
        all_indivial_inputs = response.xpath('//input|//textarea')
        for inputs in all_indivial_inputs:
            current_indivial_input = CrawledInputs()
            current_indivial_input['source_url'] = response.url
            extract_name = inputs.xpath('@id').extract()
            current_indivial_input['id'] = extract_name[0] if len(extract_name)>0 else None
            extract_name = inputs.xpath('@name').extract()
            current_indivial_input['name'] = extract_name[0] if len(extract_name)>0 else None
            extract_name = inputs.xpath('@class').extract()
            current_indivial_input['style_class'] = extract_name[0] if len(extract_name)>0 else None
            extract_name = inputs.xpath('@type').extract()
            current_indivial_input['type'] = extract_name[0] if len(extract_name)>0 else None
            extract_name = inputs.xpath('@value').extract()
            current_indivial_input['value'] = extract_name[0] if len(extract_name)>0 else None
            indivial_input_list.append(current_indivial_input)

        all_form = response.xpath('//form')
        for forms in all_form:
            current_form = CrawledForm()
            current_form['inputs'] = []
            extract_name = forms.xpath('@method').extract()
            current_form['request_method'] = extract_name[0] if len(extract_name)>0 else None
            extract_name = forms.xpath('@action').extract()
            current_form['action'] = extract_name[0] if len(extract_name) > 0 else None
            # 抛弃外链表单
            if (urlparse(current_form['action']).netloc != self.allowed_domain): continue

            this_form_inputs = forms.xpath('input|textarea')
            for this_form_input in this_form_inputs:
                this_form_input_item =  CrawledInputs()
                this_form_input_item['source_url'] = response.request.url
                extract_name = this_form_input.xpath('@id').extract()
                this_form_input_item['id'] = extract_name[0] if len(extract_name) > 0 else None
                extract_name = this_form_input.xpath('@name').extract()
                this_form_input_item['name'] = extract_name[0] if len(extract_name) > 0 else None
                extract_name = inputs.xpath('@class').extract()
                current_indivial_input['style_class'] = extract_name[0] if len(extract_name) > 0 else None
                extract_name = this_form_input.xpath('@type').extract()
                this_form_input_item['type'] = extract_name[0] if len(extract_name) > 0 else None
                extract_name = this_form_input.xpath('@value').extract()
                this_form_input_item['value'] = extract_name[0] if len(extract_name) > 0 else None
                current_form['inputs'].append(this_form_input_item)

                #去重
                if (this_form_input_item in indivial_input_list): indivial_input_list.remove(this_form_input_item)

            form_list.append(current_form)
        return form_list,indivial_input_list
