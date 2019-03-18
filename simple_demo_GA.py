# 生成攻击向量的遗传算法简明demo
# 为方便理解，这里仅设定2个混淆变异基因型：标签闭合/打开，转码
# __in代表了在其他模块中获取的必要信息。

def __in_gen_type(object):
    name = ''       #该基因的名称
    desp = ''       #对该基因的额外描述
    bits = ''       #该基因位宽
    value = 0      #增加该基因后，攻击向量强度的变化
    def parse(vector):    #将该基因表现的特征赋予攻击向量的操作
        return vector

    def unparse(vector):    #将该基因
        return vector

    def detect(vector):     #判断攻击向量是否具有该基因

def __in_gen_capital(__in_gen_type):
    name = '大小写混淆'
    desp = '拥有该基因型的攻击向量，大小写字母是随机的，以绕过区分大小写的XSS过滤检测\
            位宽为2：01代表全大写的攻击向量，10代表大小写随机的攻击向量，00代表全小写的攻击向量'
    bits = '2'
    value = 50

    def parse(vector):


def __in_gen_character_escape(__in_gen_type):
    name = '转义'
    desp = '利用转义字符绕过对xss向量的检测，例如将<替换为&lt;为\'增加转义字符等等\
           位宽为3：三位独立，1XX代表对<进行转义，X1X代表对>进行转义，XX1代表对斜杠增加双斜杠进行转义'
    bits = '3'
    value = 20


__in_basevector = ['<SCRIPT SRC=alert(\'XSS\')></SCRIPT>','<IMG SRC="jav&#x09;ascript:alert(\'XSS\');">']





