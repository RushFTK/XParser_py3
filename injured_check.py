# encoding:utf-8

from selenium import webdriver
import time

def checkalter_example(url):

    driver = webdriver.Chrome('drivers/chromedriver')
    driver.get(url)
    driver.switch_to.frasme("iframeResult")
    driver.find_element_by_xpath("html/body/input").click()
    time.sleep(1)
    al = driver.switch_to_alert()
    time.sleep(1)
    al.accept()

if __name__ == '__main__':
    # checkalter_example("http://www.runoob.com/try/try.php?filename=tryjs_alert")
    checkalter_example("http://www.baidu.com")