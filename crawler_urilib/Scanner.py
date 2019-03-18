from selenium.common import exceptions as selenium_exceptions
from selenium import webdriver
import time
from time import sleep
import re
from bs4 import BeautifulSoup

#------------------Tag.py--------------------
class Action:
    def __init__(self, path, params):
        self.path = path
        self.params = params

class Form:
    def __init__(self, host, action, id, method, name, inputs):
        self.host = host
        self.action = action if action.startswith("http") else host + action  # �ݶ�
        self.id = id
        self.method = method
        self.name = name
        self.inputs = inputs

    def __str__(self):
        s = "<form action='%s' id='%s' method='%s' name='%s'>\n" % (self.action, self.id, self.method, self.name)
        for input, input in enumerate(self.inputs):
            s += '\t' + str(input) + '\n'
        s += "</form>"
        return s

class Input:
    def __init__(self, id, name, type, value):
        self.id = id
        self.name = name
        self.type = type
        self.value = value

    def __str__(self):
        return "<input id='%s' name='%s' type='%s', value='%s'>" % (self.id, self.name, self.type, self.value)
#-----------------------------------

if __name__ == '__main__':
    target_url = 'http://xss-quiz.int21h.jp/'
    __host =
    __inputs = []
    __forms = []

    browser_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    #browser_options.add_argument('headless')
    browser_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(r'E:/GitHubClone/XParser_py3/drivers/chromedriver.exe', chrome_options=browser_options)
    driver.set_page_load_timeout(30)
    driver.get(target_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    #获取表单与信息，刘源 __getInputsAndForms(self, soup):
    bs_inputs = soup.find_all('input')
    for bs_input in bs_inputs:
        id = bs_input['id'] if 'id' in bs_input.attrs else ''
        name = bs_input['name'] if 'name' in bs_input.attrs else ''
        type = bs_input['type'] if 'type' in bs_input.attrs else ''
        value = bs_input['value'] if 'value' in bs_input.attrs else ''
        __inputs.append(Input(id, name, type, value))

    bs_forms = soup.find_all('form')
    for bs_form in bs_forms:
        form_inputs = []
        bs_inputs = bs_form.find_all('input')
        for bs_input in bs_inputs:
            id = bs_input['id'] if 'id' in bs_input.attrs else ''
            name = bs_input['name'] if 'name' in bs_input.attrs else ''
            type = bs_input['type'] if 'type' in bs_input.attrs else ''
            value = bs_input['value'] if 'value' in bs_input.attrs else ''
            form_inputs.append(Input(id, name, type, value))
        action = bs_form['action'] if 'action' in bs_form.attrs else ''
        id = bs_form['id'] if 'id' in bs_form.attrs else ''
        method = bs_form['method'] if 'method' in bs_form.attrs else ''
        name = bs_form['name'] if 'name' in bs_form.attrs else ''
        __forms.append(Form(__host, action, id, method, name, form_inputs))

    print(soup)


