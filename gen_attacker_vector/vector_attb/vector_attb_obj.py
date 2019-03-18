# vector_attb_obj.py : 攻击向量特征的基类
class vector_attb_obj(object):
    def __init__(self):
        self.order = -1              # 基因在基因编码的位置
        self.if_basic = False       # 是否是基础的特征
        self.re = ""                 # 识别该特征使用的正则表达式

    def encoding(origional_string):
    # 将原始的攻击向量编码为拥有该特征的攻击向量
        return origional_string

    def decoding(source_string):
    # 将拥有该特征的攻击向量还原为
        return source_string