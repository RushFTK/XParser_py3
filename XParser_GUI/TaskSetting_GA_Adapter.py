#-*- coding:utf-8 -*-

import sys

import XParser_GUI.TaskSetting_GA
from PyQt5 import QtCore, QtGui, QtWidgets

class TaskSetting_GA_Adapter(QtWidgets.QDialog):
    def __init__(self):
        super(TaskSetting_GA_Adapter,self).__init__()
        self.ui = XParser_GUI.TaskSetting_GA.Ui_Dialog()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Windows = TaskSetting_GA_Adapter()
    Windows.show()
    sys.exit(app.exec_())