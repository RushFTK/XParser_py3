import run_crawler
import outer_API
from file_controller import cache_cleaner
import Simluation_Attacker

def demo_non_get_post_check():
    outer_API.reset_mutillidae_db() #重置数据库，清除影响
    cleaner = cache_cleaner()
    cleaner.del_scanner_file()
    #run_crawler.run_crawler_scanner('http://owasptest.409dostastudio.pw/index.php?page=add-to-your-blog.php', depth=1)
    #run_crawler.run_crawler_scanner_splash('http://owasptest.409dostastudio.pw/index.php?page=add-to-your-blog.php', depth=1)
    run_crawler.run_crawler_scanner_splash('http://owasptest.409dostastudio.pw/index.php?page=show-log.php',
                                           depth=1)
    srequester = Simluation_Attacker.Simluation_Request()
    inv_list = srequester.load_inv_input_list()
    target_url_list = srequester.get_source_url_list(inv_list,None)
    for url in target_url_list:
        target_list_inv_input,target_list_form_input = srequester.get_same_targeturl_input(url,inv_list,None)
        inputable_inputbox = srequester.find_inputable_input_box(target_list_inv_input)
        clickbale_buttons = srequester.find_clickedable_buttons(target_list_inv_input)
        print(inputable_inputbox)
        print(clickbale_buttons)
        list_successinjuredinput = []
        if (len(inputable_inputbox) > 0 and len(clickbale_buttons) > 0):
            list_successinjuredinput, flag = srequester.check_inv_input_list_nonhidden('<script>alert(\\\'xss\\\')</script>',inputable_inputbox,clickbale_buttons)
        print(list_successinjuredinput)

if __name__ == '__main__':
    #run_crawler()
    #attacker = Simluation_Attacker()
    #attacker.form_attacker()
    demo_non_get_post_check()