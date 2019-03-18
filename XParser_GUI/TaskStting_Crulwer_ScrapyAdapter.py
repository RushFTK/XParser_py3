#-*- coding:utf-8 -*-

import sys

import XParser_GUI.TaskSetting_Cruwler_Scrapy
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TaskSetting_Crulwer_ScrapyAdapter(QtWidgets.QDialog):
    def __init__(self):
        super(TaskSetting_Crulwer_ScrapyAdapter,self).__init__()
        self.ui = XParser_GUI.TaskSetting_Cruwler_Scrapy.Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Windows = TaskSetting_Crulwer_ScrapyAdapter()
    Windows.show()
    sys.exit(app.exec_())