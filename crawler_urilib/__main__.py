from urllib import request
from lxml import etree

class simple_crawler():
    def __init__(self):
        self.target_url = [];
        self.scan_deep = 0;
        self.running = False;

    def init_baseurl(self,baseurl = ""):
        self.target_url = [baseurl]

if __name__ == '__main__':
    response = request.urlopen('http://tester1.409dostastudio.work/');
    html_body = response.read()
    doc = etree.HTML(html_body)
    decode_flag = doc.xpath('//meta[@charset]/@charset')
    html_body = html_body.decode(decode_flag[0])
    doc = etree.HTML(html_body)
    print(html_body)