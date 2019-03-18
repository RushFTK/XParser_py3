from datetime import date

class xssed_items():
    def __init__(self):
        self.full_urls = ''       # 实际的全部链接
        self.vector = ''          # 实际注入的攻击向量
        self.date = date.today()  # 日期
        self.eventhander = 0      # 该攻击向量是否为事件驱动的