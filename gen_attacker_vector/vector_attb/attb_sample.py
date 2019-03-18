from gen_attacker_vector.vector_attb import vector_attb_obj
# attb_sample.py : 一个定义攻击向量特征的示例
class attb_sample(vector_attb_obj):
    def __init__(self):
        super(attb_sample,self).__init__()
        self.order = 1 #基因编码的位置，从最低位开始数
        self.if_basic = True  # 是否是基础的特征
        self.re = ""  # 识别该特征使用的正则表达式

    def encoding(origional_string):
    # 将原始的攻击向量编码为拥有该特征的攻击向量
        return origional_string

    def decoding(source_string):
    # 将拥有该特征的攻击向量还原为
        return source_string
