import os
import subprocess
from test_windowssupport import *
from scrapy.cmdline import execute
#crawlerRunner运行
from twisted.internet import reactor
import scrapy
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging

def run_crawler(relative_path,start_url='',depth=None,other_options=None):
    # 检查配置环境
    (perp_state, prep_reason) = environment_tester()
    # 通过Scrapy下载目标文件
    location = os.path.dirname(os.path.realpath(__file__))
    exec_order = 'cd ' + location + relative_path
    if (start_url != ''):
        exec_order +=  ' -a start_urls=' + start_url
    if (depth != None):
        exec_order += ' -s DEPTH_LIMIT=' + str(depth)
    if (other_options != None):
        exec_order += ' -a ' + other_options
    # exec_order = 'cd ' + location +  '\crawler_scrapy & dir'
    print(exec_order)
    result = subprocess.call(exec_order, shell=True)
    # if (result == 1):
        #execute('scrapy crawl test -a testitem=test')
        #execute(['scrapy', 'crawl', 'test',"-a","start_urls="+ start_url])
    return 0

def run_crawler_simple_tester():
    this_start_url = 'http://tester1.409dostastudio.work/'
    this_relative_path = '\crawler_scrapy & scrapy crawl test'
    run_crawler(this_relative_path,this_start_url)

def run_crawler_database_updater():
    this_relative_path = '\database_updater\crawler & scrapy crawl xssed_index_spider'
    run_crawler(this_relative_path)


def run_crawler_scanner(scanned_url,depth):
    this_relative_path = '\crawler_scanner & scrapy crawl scanner'
    run_crawler(this_relative_path,start_url = scanned_url, depth = depth)

def run_crawler_scanner_splash(scanned_url,depth):
    this_relative_path = '\crawler_scanner & scrapy crawl scanner_splash'
    run_crawler(this_relative_path,start_url = scanned_url, depth = depth)

def run_crawler_database_update_ByRunner():
    pass

if __name__ == '__main__':
    #run_crawler_database_updater()
    #run_crawler_simple_tester()
    # run_crawler_scanner('http://xss-quiz.int21h.jp/')
    #run_crawler_scanner('http://owasptest.409dostastudio.pw/index.php?page=add-to-your-blog.php',2)
    run_crawler_scanner_splash('http://owasptest.409dostastudio.pw/index.php?page=add-to-your-blog.php',depth=1)
    #run_crawler_scanner_splash('https://awbw.amarriner.com', 0)