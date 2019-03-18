from selenium.common import exceptions as selenium_exceptions
from selenium import webdriver
from time import sleep
import re

def check_attacksuccess_byfindalter(target_url,background = True,no_image = True):
    detect_success = False
    browser_options = webdriver.ChromeOptions()
    if (background == True): browser_options.add_argument('headless')
    if (no_image == True):
        prefs = {"profile.managed_default_content_settings.images": 2}
        browser_options.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(r'E:/GitHubClone/XParser_py3/drivers/chromedriver.exe',chrome_options=browser_options)
    driver.get(target_url)
    detect_success = check_if_drivers_exist(driver)
    driver.quit()

    if (detect_success):
        return "run_success","injured_success"
    else:
        return "run_success", "injured_fail"

def check_if_drivers_exist(driver):
    try:
        target = driver.switch_to.alert
        target_re = re.match('alter\(\'[0-9a-zA-Z]*\'\)', 'alter(\'xss\')')
        if (target == None):
            detect_success = False
        else:
            detect_success = True
    except selenium_exceptions.NoAlertPresentException:
        detect_success = False
    return detect_success

if __name__ == "__main__":
    returns = check_attacksuccess_byfindalter('http://xss-quiz.int21h.jp/' , background=False)
    #进行尝试注入
    print(returns)

    # flag_maintest = True;
    # if (flag_maintest):
    #     driver = webdriver.Chrome(r'E:/GitHubClone/XParser_py3/drivers/chromedriver.exe')
    #     # driver = webdriver.Chrome('/')
    #     driver.minmize_window()
    #     driver.get('http://tester1.409dostastudio.work/see_sql.php')
    #     target = driver.switch_to.alert
    #     sleep(1)
    #     print (target.text)
    #     target.accept()
    #     sleep(1)
    #     driver.quit()
    # else:
    #     target = re.match('alter\(\'[0-9a-zA-Z]*\'\)', 'alter(\'xss\')')
    #     if (target == None):
    #         print('Not Match')
    #     else:
    #         print('')

