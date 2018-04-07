# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GeneralOutput.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(480, 360)
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(False)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 10, 461, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.MessageBrowser = QtWidgets.QTextEdit(self.layoutWidget)
        self.MessageBrowser.setEnabled(True)
        self.MessageBrowser.setAcceptDrops(False)
        self.MessageBrowser.setStyleSheet("")
        self.MessageBrowser.setReadOnly(True)
        self.MessageBrowser.setOverwriteMode(False)
        self.MessageBrowser.setObjectName("MessageBrowser")
        self.verticalLayout.addWidget(self.MessageBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_savelog = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_savelog.setObjectName("pushButton_savelog")
        self.horizontalLayout.addWidget(self.pushButton_savelog)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        self.pushButton_hide = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_hide.setObjectName("pushButton_hide")
        self.horizontalLayout.addWidget(self.pushButton_hide)
        self.pushButton_close = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_close.setObjectName("pushButton_close")
        self.horizontalLayout.addWidget(self.pushButton_close)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "通用输出窗口"))
        self.MessageBrowser.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ff0000;\">错误</span>：未以初始化方式打开界面</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600; color:#ffaa00;\">警告</span>：可能由于前述方法调用错误导致未打开信息界面，继续运行可能会造成故障</p></body></html>"))
        self.pushButton_savelog.setText(_translate("Dialog", "存储输出(&S)"))
        self.pushButton_clear.setText(_translate("Dialog", "清空(&C)"))
        self.pushButton_hide.setText(_translate("Dialog", "隐藏"))
        self.pushButton_close.setText(_translate("Dialog", "关闭(&L)"))

