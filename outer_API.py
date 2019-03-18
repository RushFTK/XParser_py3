from selenium.common import exceptions as selenium_exceptions
from selenium import webdriver
import os
import re
import time

def reset_mutillidae_db():
    browser_options = webdriver.ChromeOptions()
    prefs = {"profile.managed_default_content_settings.images": 2}
    browser_options.add_experimental_option("prefs", prefs)
    browser_options.add_argument('headless')
    driver = webdriver.Chrome(r'%s/drivers/chromedriver.exe' % os.path.dirname(__file__), chrome_options=browser_options)
    driver.get('http://owasptest.409dostastudio.pw/index.php')
    driver.find_element_by_xpath('//a[contains(@href,\'set-up-database.php\')]').click()
    try:
        target = driver.switch_to.alert
        target_re = re.match('No PHP or MySQL errors were detected when resetting the database', target.text)
        target.accept()
    except selenium_exceptions.NoAlertPresentException:
        driver.quit()
        return "reset_fail"
    driver.quit()
    if (target_re == None): return "reset_fail"
    else:                   return "reset_success"

if __name__ == "__main__":
    print(reset_mutillidae_db())