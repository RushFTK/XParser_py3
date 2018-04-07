#-*- coding:utf-8 -*-

import sys

import XParser_GUI.GeneralOutput
from PyQt5 import QtCore, QtGui, QtWidgets

class GeneralOutputAdapter(QtWidgets.QDialog):
    """
         成员变量:
         ui :                   该窗体的界面元素
         log_dialog :           该窗体所关联的"日志对话框"窗体对象
         flag_running :         本窗体是否处于运行状态
     """
    def __init__(self):
        super(GeneralOutputAdapter,self).__init__()
        self.ui = XParser_GUI.GeneralOutput.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_savelog.clicked.connect(self.savelog)
        self.ui.pushButton_clear.clicked.connect(self.clear_all_message)
        self.ui.pushButton_close.clicked.connect(quit)
        self.flag_running = False
        self.clear_all_message()

    def showEvent(self, QShowEvent):
        pass

    def add_error_message(self,message="[未定义的错误内容]"):
        """显示一条错误级别的信息，在原有信息的下方"""
        gened_message = '<span style=" font-weight:600; color:#ff0000;">错误</span>：'+message
        self.add_message(gened_message)

    def add_warning_message(self,message="[未定义的警告内容]"):
        """显示一条警告级别的信息，在原有信息的下方"""
        gened_message = '<span style=" font-weight:600; color:#ffaa00;">警告</span>：'+message
        self.add_message(gened_message)

    def add_info_message(self,message="[未定义的提示内容]"):
        """显示一条普通级别的信息，在原有信息的下方"""
        gened_message = '<span style=" font-weight:600;">信息</span>：'+message
        self.add_message(gened_message)

    def add_message(self,message="[未定义的信息]"):
        """在原有信息的下一行显示一条新的信息"""
        former_body = self.get_message(type = 'html_body')
        # self.ui.MessageBrowser.setHtml(former_body+ '<p margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;>' + message + '</p>')
        self.ui.MessageBrowser.setHtml(former_body + '<li>' + message + '</li>')

    def get_message(self, type ='text'):
        """获取文本框内容"""
        if (type == 'html'):
            return self.ui.MessageBrowser.toHtml()
        if (type == 'html_body'):
            return self.ui.MessageBrowser.toHtml().split("""<body style=" font-family:'SimSun'; font-size:9pt; font-weight:400; font-style:normal;">""")[1].split("""</body>""")[0]
        if (type == 'text'):
            return self.ui.MessageBrowser.toPlainText()
        raise Exception("get_message 错误:无效的参数type(="+type+")")

    def savelog(self):
        """存储日志"""
        savefiledialog = QtWidgets.QFileDialog()
        filename = savefiledialog.getSaveFileName(caption='输出日志另存为...', filter="*.txt;; *.log")
        self.add_info_message('存储日志至:' + filename[0])
        print(filename)

    def clear_all_message(self):
        """清空消息窗口中的原有内容"""
        self.ui.MessageBrowser.clear()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Windows = GeneralOutputAdapter()
    Windows.show()
    sys.exit(app.exec_())