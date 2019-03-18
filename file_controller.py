import os

# -*- coding: utf-8 -*-
#file controller: manage file read/write in this project
class weblist_filemanager():
    '管理存储页面列表的文件的读写'
    def __init__(self):
        self.weblist = []

    def savelist(self,target_list):
        with open('injured_input_list.json', 'a') as f:
            self.weblist_file = f

class cache_cleaner():
    '提供清除临时下载文件的方法'

    def del_scanner_file(self):
        '删除查找到的注入点信息'
        injured_form_list_path = '%s/crawler_scanner/injured_form_list.json' % os.path.dirname(__file__)
        injured_input_list_path = '%s/crawler_scanner/injured_input_list.json' % os.path.dirname(__file__)
        if os.path.exists(injured_form_list_path):
            os.remove(injured_form_list_path)
        if os.path.exists(injured_input_list_path):
            os.remove(injured_input_list_path)
        #% s / crawler_scanner / 'injured_form_list.json' % os.path.dirname(__file__)

if __name__ == '__main__':
    cleaner = cache_cleaner()
    cleaner.del_scanner_file()
