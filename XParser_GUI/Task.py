# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Task.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(691, 548)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 520, 681, 25))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.progressBar = QtWidgets.QProgressBar(self.layoutWidget)
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.horizontalLayout.addWidget(self.progressBar)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 671, 101))
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget1 = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 651, 61))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_2)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_3.addWidget(self.pushButton_6)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_4.addWidget(self.label_3)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_3.setMaxVisibleItems(5)
        self.comboBox_3.setInsertPolicy(QtWidgets.QComboBox.InsertAtBottom)
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_4.addWidget(self.comboBox_3)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_4.addWidget(self.pushButton_7)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setCheckable(False)
        self.pushButton_8.setAutoDefault(False)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_4.addWidget(self.pushButton_8)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.groupBox_2 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 130, 661, 141))
        self.groupBox_2.setObjectName("groupBox_2")
        self.pushButton_9 = QtWidgets.QPushButton(self.groupBox_2)
        self.pushButton_9.setGeometry(QtCore.QRect(10, 20, 141, 21))
        self.pushButton_9.setObjectName("pushButton_9")
        self.widget = QtWidgets.QWidget(self.groupBox_2)
        self.widget.setGeometry(QtCore.QRect(10, 80, 280, 49))
        self.widget.setObjectName("widget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.checkBox = QtWidgets.QCheckBox(self.widget)
        self.checkBox.setChecked(True)
        self.checkBox.setObjectName("checkBox")
        self.verticalLayout_2.addWidget(self.checkBox)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        self.comboBox_4 = QtWidgets.QComboBox(self.widget)
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_5.addWidget(self.comboBox_4)
        self.pushButton_10 = QtWidgets.QPushButton(self.widget)
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_5.addWidget(self.pushButton_10)
        self.verticalLayout_2.addLayout(self.horizontalLayout_5)
        self.widget1 = QtWidgets.QWidget(self.groupBox_2)
        self.widget1.setGeometry(QtCore.QRect(10, 50, 195, 22))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.widget1)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.groupBox_3 = QtWidgets.QGroupBox(Dialog)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 280, 661, 81))
        self.groupBox_3.setObjectName("groupBox_3")
        self.layoutWidget2 = QtWidgets.QWidget(self.groupBox_3)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 20, 312, 49))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.checkBox_2 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_6.addWidget(self.checkBox_2)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_6.addWidget(self.lineEdit)
        self.pushButton_setoutputdirectory = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_setoutputdirectory.setObjectName("pushButton_setoutputdirectory")
        self.horizontalLayout_6.addWidget(self.pushButton_setoutputdirectory)
        self.verticalLayout_3.addLayout(self.horizontalLayout_6)
        self.checkBox_3 = QtWidgets.QCheckBox(self.layoutWidget2)
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setObjectName("checkBox_3")
        self.verticalLayout_3.addWidget(self.checkBox_3)

        self.retranslateUi(Dialog)
        self.comboBox_3.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "XSS漏洞检测 - 详细设定"))
        self.pushButton.setText(_translate("Dialog", "开始"))
        self.pushButton_2.setText(_translate("Dialog", "显示信息"))
        self.groupBox.setTitle(_translate("Dialog", "攻击向量生成"))
        self.label_2.setText(_translate("Dialog", "攻击向量列表选择"))
        self.comboBox_2.setItemText(0, _translate("Dialog", "ExampleList.vectorlist"))
        self.comboBox_2.setItemText(1, _translate("Dialog", "Downloaded.vectorlist"))
        self.pushButton_5.setText(_translate("Dialog", "更新向量列表"))
        self.pushButton_6.setText(_translate("Dialog", "从库下载"))
        self.label_3.setText(_translate("Dialog", "攻击向量扩展方法"))
        self.comboBox_3.setItemText(0, _translate("Dialog", "不使用任何扩展方法"))
        self.comboBox_3.setItemText(1, _translate("Dialog", "使用简单遗传算法进行扩展"))
        self.pushButton_7.setText(_translate("Dialog", "更新扩展方法列表"))
        self.pushButton_8.setText(_translate("Dialog", "属性"))
        self.groupBox_2.setTitle(_translate("Dialog", "注入点查找"))
        self.pushButton_9.setText(_translate("Dialog", "设定注入点网址列表...."))
        self.checkBox.setText(_translate("Dialog", "使用分析模块寻找额外注入点"))
        self.label_4.setText(_translate("Dialog", "分析模块"))
        self.comboBox_4.setItemText(0, _translate("Dialog", "Scrapy v1.5 + Xpath"))
        self.comboBox_4.setItemText(1, _translate("Dialog", "Urilib + Xpath"))
        self.pushButton_10.setText(_translate("Dialog", "属性"))
        self.label.setText(_translate("Dialog", "Cookies："))
        self.groupBox_3.setTitle(_translate("Dialog", "结果处理"))
        self.checkBox_2.setText(_translate("Dialog", "输出日志至..."))
        self.pushButton_setoutputdirectory.setText(_translate("Dialog", "选择文件夹..."))
        self.checkBox_3.setText(_translate("Dialog", "将使用向量上传至库"))

