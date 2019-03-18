import scrapy

class testspider(scrapy.Spider):
    name = "test"
    allowed_domains = '409dostastudio.work'
    url_lists = []
    injured_words = []

    def __init__(self, start_urls=None, *args, **kwargs):
        super(eval(self.__class__.__name__), self).__init__(*args, **kwargs)
        self.start_url = start_urls
        testspider.url_lists.append(start_urls)

    def start_requests(self):
        yield scrapy.Request(self.start_url, self.parse)
        #yield scrapy.Request('http://tester2.409dostastudio.work/', self.parse)

    def parse(self, response):
        contents = response.xpath('//input[@name]/@name').extract()
        for word in contents:
            testspider.injured_words.append(word)

        ifnonewurls = 1
        testspider.url_lists.append(response.url)
        #get all request page
        urls = response.xpath('//@href').extract()
        for path_url in urls:
            if len(path_url.split('/'))> 1:
                url_dirs = path_url.split('/')[1:]
                real_url = response.url
                for index in range(len(url_dirs)):
                    real_url += url_dirs[index]
                    if index != (len(url_dirs)-1):
                        real_url += '/'
                    if (index == (len(url_dirs)-1)) and (len(url_dirs[index].split('.'))<=1):
                        real_url += '/'
                self.log('Get url - %s' % real_url)
                if not real_url in testspider.url_lists:
                    ifnonewurls = 0
                    yield scrapy.Request(response.urljoin(real_url))

        print("testspider.target_list=")
        print(testspider.injured_words)


        #confirm saved page title
        # page_name = response.url
        # if (page_name.split('/')[-1]) is not "":
        #     filename = 'test-%s-%s.html' % (page_name.split('/')[-3] , page_name.split('/')[-1])
        # else:
        #     filename = 'test-%s.html' % page_name.split('/')[-2]

        #confirm saved url

        if ifnonewurls:
            with open('url_list.txt', 'w') as f:
                for urls in testspider.url_lists:
                    f.write(urls + '\n')
                f.close()
            self.log('Saved url_list')
            with open('target_list.txt','w') as f:
                for word in testspider.injured_words:
                    f.write(word + '\n')
                f.close()
            self.log('Saved target_list')

    #get context
    def parseContent(self, response):

        pass