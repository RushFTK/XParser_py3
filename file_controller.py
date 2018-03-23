# -*- coding: utf-8 -*-
#file controller: manage file read/write in this project
class weblist_filemanager
    '管理存储页面列表的文件的读写'
    def __init__(self):
        self.weblist = []


    def savelist(self,target_list):
        self.weblist_file = file.open("weblist.txt", "wb")



