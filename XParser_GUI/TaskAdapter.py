#-*- coding:utf-8 -*-

import sys

import XParser_GUI.Task
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *

class TaskAdapter(QtWidgets.QDialog):
    def __init__(self):
        super(TaskAdapter,self).__init__()
        self.ui = XParser_GUI.Task.Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.pushButton_setoutputdirectory.clicked.connect(self.event_setdirectory)

    def event_setdirectory(self):
        dir_path = QFileDialog.getExistingDirectory(self, "选择目录", "C:\\Users\\Administrator\\Desktop")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Windows = TaskAdapter()
    Windows.show()
    sys.exit(app.exec_())