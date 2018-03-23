import os
import subprocess
from test_windowssupport import *

def run_crawler():
    # 检查配置环境
    (perp_state, prep_reason) = environment_tester()
    # 通过Scrapy下载目标文件
    location = os.path.dirname(os.path.realpath(__file__))
    exec_order = 'cd ' + location + '\crawler_scrapy & scrapy crawl test'
    # exec_order = 'cd ' + location +  '\crawler_scrapy & dir'
    print(exec_order)
    result = subprocess.call(exec_order, shell=True)
    print(result)
    return 0

if __name__ == '__main__':
    run_crawler()